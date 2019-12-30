import cv2
import numpy as np


if __name__ == '__main__':
    import os
    import sys
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ROOT_DIR = os.path.dirname(BASE_DIR)
    # sys.path.append(ROOT_DIR)  # config
    ROOT_DIR = os.path.dirname(ROOT_DIR)
    sys.path.append(ROOT_DIR)  # config
    sys.path.append(os.path.join(ROOT_DIR, 'utils')) # utils
    sys.path.append(os.path.join(ROOT_DIR, 'libs'))  # libs
    
    print(ROOT_DIR)

import src.utils.util as util
from src.Grad.Camera.camera import Camera
from src.utils.util import get_center_fast as get_center
from src.utils.model_pose_ren import ModelPoseREN


class HandPose():

    def __init__(self, fx, fy, ux, uy, lower_, upper_, dataset='hands17'):
        self.dataset = dataset
        self.hand_model = ModelPoseREN(dataset,
            lambda img: get_center(img, lower=lower_, upper=upper_),
            param=(fx, fy, ux, uy), use_gpu=True)
        if dataset == 'msra':
            self.hand_model.reset_model(dataset, test_id=0)
        self.device = Camera()

    def show_results(self, img, results, cropped_image, dataset):
        """
        for test
        """
        img = np.minimum(img, 1500)
        img = (img - img.min()) / (img.max() - img.min())
        img = np.uint8(img*255)
        # draw cropped image
        img[:96, :96] = (cropped_image+1)*255/2
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        cv2.rectangle(img, (0, 0), (96, 96), (255, 0, 0), thickness=2)
        img_show = util.draw_pose(dataset, img, results)
        return img_show

    def get_pose(self):
        self.device.start_device()

        while True:
            depth = self.device.read_frame()
            if self.dataset == 'icvl':
                depth = depth[:, ::-1]
            results, cropped_image = self.hand_model.detect_image(depth)
            img_show = self.show_results(depth, results, cropped_image, self.dataset)
            cv2.imshow('result', img_show)
            
            k = cv2.waitKey(1) & 0xFF
            if k == ord('q'):
                break
        self.device.stop_device()


if __name__ == '__main__':
    # fx, fy, ux, uy = 385.13, 385.13, 316.802, 241.818
    # lower_ = 200
    # upper_ = 450
    params = {
        'fx': 385.13, 'fy': 385.13, 'ux': 316.802, 'uy': 241.818,
        'lower_': 200, 'upper_': 450
    }
    hp = HandPose(**params)
    hp.get_pose()