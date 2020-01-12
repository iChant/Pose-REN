import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)
# sys.path.append(ROOT_DIR)  # config
ROOT_DIR = os.path.dirname(ROOT_DIR)
sys.path.append(ROOT_DIR)  # config
sys.path.append(os.path.join(ROOT_DIR, 'utils'))  # utils
sys.path.append(os.path.join(ROOT_DIR, 'libs'))  # libs

from src.utils.model_pose_ren import ModelPoseREN
from src.utils.util import get_center_fast as get_center
# from src.Grad.Camera.camera import Camera
import src.utils.util as util
import cv2
import numpy as np

from multiprocessing import Queue


class HandPose():

    def __init__(self, fx, fy, ux, uy, lower_, upper_, dataset='hands17'):
        print('Handpose: ', os.getpid())
        self.dataset = dataset
        self.hand_model = ModelPoseREN(dataset,
                                       lambda img: get_center(
                                           img, lower=lower_, upper=upper_),
                                       param=(fx, fy, ux, uy), use_gpu=True)
        if dataset == 'msra':
            self.hand_model.reset_model(dataset, test_id=0)

    def show_results(self, img, results, cropped_image, dataset):
        img = np.minimum(img, 1500)
        img = (img - img.min()) / (img.max() - img.min())
        img = np.uint8(img*255)
        img[:96, :96] = (cropped_image+1)*255/2
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        cv2.rectangle(img, (0, 0), (96, 96), (255, 0, 0), thickness=2)
        img_show = util.draw_pose(dataset, img, results)
        return img_show

    def get_pose(self, depth):
        if self.dataset == 'icvl':
            depth = depth[:, ::-1]
        results, cropped_image = self.hand_model.detect_image(depth)
        img_show = self.show_results(
            depth, results, cropped_image, self.dataset)
        return results, img_show



def run(q):
    import pyrealsense2 as rs
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    profile = pipeline.start(config)
    depth_sensor = profile.get_device().first_depth_sensor()
    depth_scale = depth_sensor.get_depth_scale()

    params = {
        'fx': 385.13, 'fy': 385.13, 'ux': 316.802, 'uy': 241.818,
        'lower_': 150, 'upper_': 550
    }
    hp = HandPose(**params)

    while True:
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        depth_image = np.asarray(depth_frame.get_data(), dtype=np.float32)
        depth = depth_image * depth_scale * 1000
        depth[depth == 0] = depth.max()
        results, img_show = hp.get_pose(depth)
        res = {'results': results, 'img_show': img_show}
        q.put(res)


if __name__ == '__main__':
    import pyrealsense2 as rs
    pipeline = rs.pipeline()
    config = rs.config()
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
    profile = pipeline.start(config)
    depth_sensor = profile.get_device().first_depth_sensor()

    preset_range = depth_sensor.get_option_range(rs.option.visual_preset)
    print(str(preset_range))
    for i in range(int(preset_range.max)):
        visulpreset = depth_sensor.get_option_value_description(rs.option.visual_preset,i)
        print('%02d: %s' % (i, visulpreset))
        if visulpreset == 'Hand':
            depth_sensor.set_option(rs.option.visual_preset, i)    

    depth_scale = depth_sensor.get_depth_scale()

    params = {
        'fx': 385.13, 'fy': 385.13, 'ux': 316.802, 'uy': 241.818,
        'lower_': 100, 'upper_': 450
    }
    hp = HandPose(**params)

    while True:
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        depth_image = np.asarray(depth_frame.get_data(), dtype=np.float32)
        depth = depth_image * depth_scale * 1000
        depth[depth == 0] = depth.max()
        results, img_show = hp.get_pose(depth)
        # res = {'results': results, 'img_show': img_show}
        # q.put(res)
        cv2.imshow('result', img_show)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('q'):
            break
    pipeline.stop()

    # # fx, fy, ux, uy = 385.13, 385.13, 316.802, 241.818
    # # lower_ = 200
    # # upper_ = 450
    # params = {
    #     'fx': 385.13, 'fy': 385.13, 'ux': 316.802, 'uy': 241.818,
    #     'lower_': 300, 'upper_': 650
    # }
    # hp = HandPose(**params)
    # # hp.start_device()
    # # while True:
    # #     results, img_show = hp.get_pose()
    # #     cv2.imshow('result', img_show)
    # #     k = cv2.waitKey(1) & 0xFF
    # #     if k == ord('q'):
    # #         break

    # # hp.stop_device()
    # # hp.get_pose()
