from fastdtw import fastdtw
import numpy as np


def dtw(x, y):
    """
    get distance for feature array x and y
    ---
    params
    x, y    arrays shaped as (point_count, frame_count)
            frame_count of x and y can be different
    ---
    return  dtw distance
    """
    assert x.shape[0] == y.shape[0], 'input' + \
        'arrays should have same shape[0]'
    p_cnt = x.shape[0]
    dists = []
    paths = []
    _, tpath = fastdtw(x.T, y.T)
    for i in range(p_cnt):
        d, p = fastdtw(x[i, :], y[i, :])
        dists.append(d)
        paths.append(p)
    return dists, paths, tpath


def get_dist(dists):
    return np.linalg.norm(dists)
