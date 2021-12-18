# pyright: strict

"""Disgustingly un-Pythonic (functional) Python"""

from typing import Optional, Tuple, Union, cast
from functools import lru_cache, reduce
from itertools import permutations, starmap

Pair = Union[int, Tuple["Pair", "Pair"]]

# 3.8 Compatibility
cache = lru_cache(maxsize=None)

def add(a: Pair, b: Pair) -> Pair:
    return pair_reduce((a, b))

def pair_reduce(pair: Pair) -> Pair:
    while True:
        _pair, adds = explode(pair)
        if adds is not None:
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
def addLeftMost(pair: Pair, n: int) -> Pair:
    if isinstance(pair, tuple):
        return (addLeftMost(pair[0], n), pair[1])
    else:
        return pair + n

@cache
def explode(pair: Pair, depth: int=0) -> Tuple[Pair, Optional[Tuple[int, int]]]:
    if isinstance(pair, int):
        return pair, None
    else: # pair is tuple
        if depth >= 4:
            _pair = cast(Tuple[int, int], pair)
            return 0, _pair
        else:
            left, right = pair
            _left, adds = explode(left, depth+1)
            if adds is not None:
                addLeft, addRight = adds
                return (_left, addLeftMost(right, addRight)), (addLeft, 0)

            _right, adds = explode(right, depth+1)
            if adds is not None:
                addLeft, addRight = adds
                return (addRightMost(left, addLeft), _right), (0, addRight)
        return pair, None

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
