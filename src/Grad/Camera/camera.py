import pyrealsense2 as rs
import numpy as np

import os

class Camera():

    def __init__(self):
        self.pipeline = rs.pipeline()

    def start_device(self):
        config = rs.config()
        config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
        profile = self.pipeline.start(config)
        depth_sensor = profile.get_device().first_depth_sensor()
        self.depth_scale = depth_sensor.get_depth_scale()


    def stop_device(self):
        self.pipeline.stop()
    
    def read_frame(self):
        frames = self.pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        depth_image = np.asarray(depth_frame.get_data(), dtype=np.float32)
        depth = depth_image * self.depth_scale * 1000
        depth[depth == 0] = depth.max()
        return depth


def test():
    camera = Camera()
    f = camera.read_frame()
    print(f)


# if __name__ == '__main__':
#     test()
