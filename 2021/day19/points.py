from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int
    z: int

    def __add__(s, o: "Point"):
        return Point(s.x + o.x, s.y + o.y, s.z + o.z)
    
    def __sub__(s, o: "Point"):
        return Point(s.x - o.x, s.y - o.y, s.z - o.z)

    def total(s):
        return abs(s.x) + abs(s.y) + abs(s.z)
    
    def rotate(s, o):
        return rotations[o](s)

rotations = [
    lambda p: Point(p.x, p.z, -p.y),
    lambda p: Point(-p.z, p.x, -p.y),
    lambda p: Point(-p.x, -p.z, -p.y),
    lambda p: Point(p.z, -p.x, -p.y),
    lambda p: Point(p.z, -p.y, p.x),
    lambda p: Point(p.y, p.z, p.x),
    lambda p: Point(-p.z, p.y, p.x),
    lambda p: Point(-p.y, -p.z, p.x),
    lambda p: Point(-p.y, p.x, p.z),
    lambda p: Point(-p.x, -p.y, p.z),
    lambda p: Point(p.y, -p.x, p.z),
    lambda p: Point(p.x, p.y, p.z),
    lambda p: Point(-p.z, -p.x, p.y),
    lambda p: Point(p.x, -p.z, p.y),
    lambda p: Point(p.z, p.x, p.y),
    lambda p: Point(-p.x, p.z, p.y),
    lambda p: Point(-p.x, p.y, -p.z),
    lambda p: Point(-p.y, -p.x, -p.z),
    lambda p: Point(p.x, -p.y, -p.z),
    lambda p: Point(p.y, p.x, -p.z),
    lambda p: Point(p.y, -p.z, -p.x),
    lambda p: Point(p.z, p.y, -p.x),
    lambda p: Point(-p.y, p.z, -p.x),
    lambda p: Point(-p.z, -p.y, -p.x)
]

double_rotations = [
    [18, 19, 16, 17, 7, 4, 5, 6, 1, 2, 3, 0, 10, 11, 8, 9, 15, 12, 13, 14, 21, 22, 23, 20],
    [23, 20, 21, 22, 17, 18, 19, 16, 2, 3, 0, 1, 5, 6, 7, 4, 14, 15, 12, 13, 11, 8, 9, 10],
    [9, 10, 11, 8, 22, 23, 20, 21, 3, 0, 1, 2, 19, 16, 17, 18, 13, 14, 15, 12, 6, 7, 4, 5],
    [4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 20, 21, 22, 23, 12, 13, 14, 15, 16, 17, 18, 19],
    [14, 15, 12, 13, 11, 8, 9, 10, 5, 6, 7, 4, 2, 3, 0, 1, 23, 20, 21, 22, 17, 18, 19, 16],
    [19, 16, 17, 18, 13, 14, 15, 12, 6, 7, 4, 5, 9, 10, 11, 8, 22, 23, 20, 21, 3, 0, 1, 2],
    [1, 2, 3, 0, 18, 19, 16, 17, 7, 4, 5, 6, 15, 12, 13, 14, 21, 22, 23, 20, 10, 11, 8, 9],
    [8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7, 16, 17, 18, 19, 20, 21, 22, 23, 12, 13, 14, 15],
    [22, 23, 20, 21, 3, 0, 1, 2, 9, 10, 11, 8, 6, 7, 4, 5, 19, 16, 17, 18, 13, 14, 15, 12],
    [15, 12, 13, 14, 21, 22, 23, 20, 10, 11, 8, 9, 1, 2, 3, 0, 18, 19, 16, 17, 7, 4, 5, 6],
    [5, 6, 7, 4, 14, 15, 12, 13, 11, 8, 9, 10, 23, 20, 21, 22, 17, 18, 19, 16, 2, 3, 0, 1],
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
    [6, 7, 4, 5, 19, 16, 17, 18, 13, 14, 15, 12, 22, 23, 20, 21, 3, 0, 1, 2, 9, 10, 11, 8],
    [11, 8, 9, 10, 5, 6, 7, 4, 14, 15, 12, 13, 17, 18, 19, 16, 2, 3, 0, 1, 23, 20, 21, 22],
    [21, 22, 23, 20, 10, 11, 8, 9, 15, 12, 13, 14, 7, 4, 5, 6, 1, 2, 3, 0, 18, 19, 16, 17],
    [16, 17, 18, 19, 20, 21, 22, 23, 12, 13, 14, 15, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7],
    [2, 3, 0, 1, 23, 20, 21, 22, 17, 18, 19, 16, 14, 15, 12, 13, 11, 8, 9, 10, 5, 6, 7, 4],
    [7, 4, 5, 6, 1, 2, 3, 0, 18, 19, 16, 17, 21, 22, 23, 20, 10, 11, 8, 9, 15, 12, 13, 14],
    [13, 14, 15, 12, 6, 7, 4, 5, 19, 16, 17, 18, 3, 0, 1, 2, 9, 10, 11, 8, 22, 23, 20, 21],
    [20, 21, 22, 23, 12, 13, 14, 15, 16, 17, 18, 19, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3],
    [10, 11, 8, 9, 15, 12, 13, 14, 21, 22, 23, 20, 18, 19, 16, 17, 7, 4, 5, 6, 1, 2, 3, 0],
    [3, 0, 1, 2, 9, 10, 11, 8, 22, 23, 20, 21, 13, 14, 15, 12, 6, 7, 4, 5, 19, 16, 17, 18],
    [17, 18, 19, 16, 2, 3, 0, 1, 23, 20, 21, 22, 11, 8, 9, 10, 5, 6, 7, 4, 14, 15, 12, 13],
    [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
]