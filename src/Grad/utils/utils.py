import numpy as np


def move_line(mat, f, t, axis=0):
    """
    move line in matrix mat from line f to line t
    """
    assert axis != 0 or axis != 1, 'axis can only be 0 or 1'
    assert f < mat.shape[axis] and t < mat.shape[axis], 'f or t is out of bound'
    if axis == 0:
        mat[f:t+1, :] = np.roll(mat[f:t+1, :], -1, axis=0)
    else:
        mat[f:t+1, :] = np.roll(mat[:, f:t+1], -1, axis=1)


def swap_line(mat, i, j, axis=0):
    """
    swap two lines in a matrix
    """
    assert axis != 0 or axis != 1, 'axis can only be 0 or 1'
    assert i < mat.shape[axis] and j < mat.shape[axis], 'indice out of bound'
    if axis == 0:
        mat[[i, j], :] = mat[[j, i], :]
    else:
        mat[:, [i, j]] = mat[:, [j, i]]


def add_line(mat, line, to, axis=0):
    """
    add line to mat
    """
    assert axis != 0 or axis != 1, 'axis can only be 0 or 1'
    assert to < mat.shape[axis], 'indice out of bound'
    # l = List()
    if axis == 0:
        # l = [mat[:to, :], line, mat[to:, :]]
        return np.vstack([mat[:to, :], line, mat[to:, :]])
    else:
        # l = [mat[:, :to], line, mat[:, to:]]
        return np.hstack([mat[:, :to], line, mat[:, to:]])


def get_max_location(arr):
    return list(map(lambda x: x == max(x), arr)) * np.ones(shape=arr.shape)


def get_nonzero_locations(x, threshold=1.5, axis=0):
    lengths = np.linalg.norm(x, axis=axis)
    return (lengths > threshold) * 1
    # return list(map(lambda arg: arg == max(arg), lengths)) * np.ones(shape=x.shape)


def running_mean(x, window_sz=5, axis=None):
    cumsum = np.cumsum(np.insert(x, 0, 0, axis=axis), axis=axis)
    return (cumsum[window_sz:] - cumsum[:-window_sz]) / float(window_sz)


def get_ith_point_ts(x, i):
    assert len(x.shape) == 3, "wrong shape of input matrix"
    return x[:, i, :]
