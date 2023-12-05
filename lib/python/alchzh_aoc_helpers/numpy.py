from enum import Enum

import numpy as np

gft = np.genfromtxt

def frozenarray(*args, **kwargs):
    arr = np.array(*args, **kwargs)
    arr.setflags(write=False)
    return arr

class Dir(Enum):
    E: frozenarray([0, 1])
    S: frozenarray([1, 0])
    W: frozenarray([0, -1])
    N: frozenarray([-1, 0])
    SE: frozenarray([1, 1])
    SW: frozenarray([1, -1])
    NW: frozenarray([-1, -1])
    NE: frozenarray([-1, 1])

def P(*args):
    return np.array(args)

def in_bounds(p, arr=None):
    if np.min(p) < 0:
        return False
    return arr is None or np.all(np.less(p, np.shape(arr)))

def neighbors(p, arr=None):
    for d in Dir:
        neighbor = p + d
        if in_bounds(neighbor, arr):
            yield neighbor