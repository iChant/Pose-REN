import logging
logging.basicConfig(level=logging.INFO)
import numpy as np
import cv2
import pyrealsense2 as rs
import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
sys.path.append(ROOT_DIR) # config
sys.path.append(os.path.join(ROOT_DIR, 'utils')) # utils
sys.path.append(os.path.join(ROOT_DIR, 'libs')) # libs
from model_pose_ren import ModelPoseREN
import util
from util import get_center_fast as get_center

from chaincode import *
from dtw import *
from draw_plot import Plotter
# import matplotlib
# matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


def read_trainset():
    dataset_list = os.listdir('dataset')
    datasets = {}
    features = {}
    for filename in dataset_list:
        datasets[filename] = np.load('dataset/' + filename)
        features[filename] = get_feature(datasets[filename])
    return datasets, features

def test(t_feat, feats):
    # d, f = read_trainset()
    res = {}
    for name in feats:
        dists, paths, tpath = dtw(feats[name], t_feat)
        res[name] = np.linalg.norm(dists)
    label = min(res, key=res.get)
    print(label)
    res_f = feats[label]
    # test_f = feats[test]
    dists, paths, tpath = dtw(feats[label], t_feat)
    if get_dist(dists) >= 600:
        label = 'None'
        p = Plotter(get_dist(dists), tpath, dists, paths, t_feat, res_f, label)
        p.show_hand_nodetail()
        plt.show()
    else:
        p = Plotter(get_dist(dists), tpath, dists, paths, t_feat, res_f, label)
        p.show_hand()
        p.show_total_features()
        plt.show()

def init_device():
    # Configure depth streams
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    print('config')
    # Start streaming
    profile = pipeline.start(config)
    depth_sensor = profile.get_device().first_depth_sensor()
    depth_scale = depth_sensor.get_depth_scale()
    print('Depth Scale is: ' , depth_scale)
    return pipeline, depth_scale

def stop_device(pipeline):
    pipeline.stop()
    
def read_frame_from_device(pipeline, depth_scale):
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    #if not depth_frame:
    #    return None
    # Convert images to numpy arrays
    depth_image = np.asarray(depth_frame.get_data(), dtype=np.float32)
    depth = depth_image * depth_scale * 1000
    return depth

def show_results(img, results, cropped_image, dataset):
    img = np.minimum(img, 1500)
    img = (img - img.min()) / (img.max() - img.min())
    img = np.uint8(img*255)
    # draw cropped image
    img[:96, :96] = (cropped_image+1)*255/2
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    cv2.rectangle(img, (0, 0), (96, 96), (255, 0, 0), thickness=2)
    img_show = util.draw_pose(dataset, img, results)
    return img_show

def main():
    # intrinsic paramters of Intel Realsense SR300
    # fx, fy, ux, uy = 463.889, 463.889, 320, 240
    fx, fy, ux, uy = 385.13, 385.13, 316.802, 241.818
    # paramters
    dataset = 'hands17'
    if len(sys.argv) == 2:
        dataset = sys.argv[1]

    lower_ = 200
    upper_ = 450

    # init realsense
    pipeline, depth_scale = init_device()
    # init hand pose estimation model
    hand_model = ModelPoseREN(dataset,
        lambda img: get_center(img, lower=lower_, upper=upper_),
        param=(fx, fy, ux, uy), use_gpu=True)
    # for msra dataset, use the weights for first split
    if dataset == 'msra':
        hand_model.reset_model(dataset, test_id=0)
        
    is_recording = False
    is_testing = False
    d, f = read_trainset()
    rec = []

    # realtime hand pose estimation loop
    while True:
        depth = read_frame_from_device(pipeline, depth_scale)
        # preprocessing depth
        depth[depth == 0] = depth.max()
        # training samples are left hands in icvl dataset,
        # right hands in nyu dataset and msra dataset,
        # for this demo you should use your right hand
        if dataset == 'icvl':
            depth = depth[:, ::-1]  # flip
        # get hand pose
        results, cropped_image = hand_model.detect_image(depth)
        img_show = show_results(depth, results, cropped_image, dataset)
        cv2.imshow('result', img_show)

        if is_recording or is_testing:
            rec.append(results)
        readkey = cv2.waitKey(1) & 0xFF

        if readkey == ord('q'):
            break

        elif readkey == ord('r'):
            if is_testing:
                print('*** cannot record ***')
            if not is_recording:
                print("--- is recording ---")
                is_recording = True
            else:
                print("--- recording stopped ---")
                is_recording = False
                filename = input('filename: ')
                np.save(filename + '.npy', rec)
                rec = []

        elif readkey & 0xFF == ord('t'):
            if is_recording:
                print('*** cannot test ***')
            if not is_testing:
                print('--- is testing ---')
                is_testing = True
            else:
                is_testing = False
                t_feat = get_feature(np.array(rec))
                rec = []
                test(t_feat, f)

    stop_device(pipeline)

if __name__ == '__main__':
    main()
