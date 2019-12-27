"""
    链码基向量选择：
    1. F26
    2. 链码基向量需要满足条件，即相似方向尽可能相邻，相反方向尽可能远。
    链码方向代码值的相对大小在序列中有实际意义（影响序列的 DTW 距离），
    方向相近的值大小也应该尽可能相近（与传统的图形学中弗里曼链码侧重点不同）。 
"""

import numpy as np
import numba


if __name__ == '__main__':
    from utils import *
else:
    from utils.utils import *


def _get_base_vector():
    bin_base = np.array([[1, 0], [1, -1], [0, -1], [-1, -1],
                         [-1, 0], [-1, 1], [0, 1], [1, 1]])
    z = [0, 1, -1]
    base_vectors = [
        np.hstack((bin_base, i * np.ones((bin_base.shape[0], 1)))) for i in z]
    base_vectors[1] = np.roll(base_vectors[1], 4, axis=0)
    base_vector = np.vstack(base_vectors)
    for i in range(4):
        move_line(base_vector, 3 - i, -9)
    base_vector = add_line(base_vector, np.array([0, 0, 1]), 5)
    base_vector = add_line(base_vector, np.array([0, 0, -1]), -7)
    return (base_vector.T / np.linalg.norm(base_vector, axis=1))


base_vector = _get_base_vector()


def _get_feature(point_ts):
    """
    @param  point_ts point time serial, shape of (frame_count, point_axis_count)
    @return array shape as (frame_count - moving_window_sz, 1)
    """
    frame_count = point_ts.shape[0]
    point_axis_count = point_ts.shape[1]
    feature_labels = np.array([i + 1 for i in range(base_vector.shape[1])])
    delta = point_ts[1:, :] - point_ts[:-1, :]
    delta = running_mean(delta, window_sz=6, axis=0)
    nonzero_loc = get_nonzero_locations(delta, axis=1)
    dir_values = delta.dot(base_vector)
    features = get_max_location(dir_values).dot(feature_labels)
    return features * nonzero_loc


def get_feature(points_ts):
    """
    @param  points_ts array of points in time serial, shape
            as (frame_count, point_count, point_axis_count)

    @return array shape as (frame_count - moving_window_sz,
            point_count)
    """
    l = [_get_feature(get_ith_point_ts(points_ts, i))
         for i in range(points_ts.shape[1])]
    return np.array(l)
