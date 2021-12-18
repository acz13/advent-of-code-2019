# pyright: strict

"""Disgustingly un-Pythonic (functional) Python"""

from typing import Tuple, Union
from functools import lru_cache, reduce
from itertools import permutations, starmap

Pair = Union[int, Tuple["Pair", "Pair"]]

# 3.8 Compatibility
cache = lru_cache(maxsize=None)

def add(a: Pair, b: Pair) -> Pair:
    return pair_reduce((a, b))

def pair_reduce(pair: Pair) -> Pair:
    while True:
        _pair, actionable, _, _ = explode(pair)
        if not actionable:
            pair = _pair
            continue
        _pair, actionable = split(_pair)
        if not actionable:
            pair = _pair
            continue
        return _pair

@cache
def addRightMost(pair: Pair, n: int) -> Pair:
    if isinstance(pair, tuple):
        return (pair[0], addRightMost(pair[1], n))
    else:
        return pair + n

@cache
def explode(pair: Pair, depth: int=0, actionable: bool=True, rightAdd: int=0) -> Tuple[Pair, bool, int, int]:
    if isinstance(pair, int):
        return pair+rightAdd, actionable, 0, 0
    else: # pair is tuple
        if depth >= 4 and actionable:
            if not (isinstance(pair[0], int) and isinstance(pair[1], int)):
                print(pair)
                raise ValueError()
            return 0, False, pair[0], pair[1]
        else:
            left, actionable, leftAdd1, rightAdd = explode(pair[0], depth+1, actionable, rightAdd)
            right, actionable, leftAdd2, rightAdd = explode(pair[1], depth+1, actionable, rightAdd)
            if leftAdd2 != 0:
                left = addRightMost(left, leftAdd2)
            return (left, right), actionable, leftAdd1, rightAdd

@cache
def split(pair: Pair, actionable: bool=True) -> Tuple[Pair, bool]:
    if isinstance(pair, int):
        if pair > 9 and actionable:
            return (pair // 2, pair // 2 + pair % 2), False
        else:
            return pair, actionable
    else: # pair is tuple
        left, actionable = split(pair[0], actionable)
        right, actionable = split(pair[1], actionable)
        return (left, right), actionable

@cache
def magnitude(pair: Pair) -> int:
    if isinstance(pair, int):
        return pair
    else: # pair is tuple
        return 3*magnitude(pair[0]) + 2*magnitude(pair[1])

def str_to_pair(s: str) -> Pair:
    return eval(s.strip().replace("[", "(").replace("]", ")"))

def str_from_pair(s: Pair) -> str:
    return str(s).replace("(", "[").replace(")", "]").replace(" ", "")

pairs = [str_to_pair(line) for line in open(0).readlines()]

print(" -- Part 1 -- ")
sum1 = reduce(add, pairs)
print("Final sum:", str_from_pair(sum1))
print("Magnitude:", magnitude(sum1))

print(" -- Part 2 -- ")
mag2, sum2 = max((magnitude(x), x) for x in starmap(add, permutations(pairs, 2)))
print("Final sum:", str_from_pair(sum2))
print("Magnitude:", mag2)
