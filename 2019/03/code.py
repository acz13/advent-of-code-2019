# Advent of code Year 2019 Day 3 solution
# Author = Albert Zhang
# Date = December 2019

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

[wire1, wire2] = map(lambda x: x.split(","), input.split("\n"))

def dist(p):
    return abs(p[0]) + abs(p[1])

w1p = set()
w2p = set()

w1steps = {}
w2steps = {}


def process(wire, s, lens):
    point = (0, 0)
    stepsTo = 0
    for i in wire:
        d = i[0]
        l = int(i[1:])
        if d == 'R':
            for i in range(l):
                point = (point[0] + 1, point[1])
                s.add(point)
                stepsTo += 1
                if point not in lens:
                    lens[point] = stepsTo
        elif d == 'L':
            for i in range(l):
                point = (point[0] - 1, point[1])
                s.add(point)
                stepsTo += 1
                if point not in lens:
                    lens[point] = stepsTo
        elif d == 'D':
            for i in range(l):
                point = (point[0], point[1] + 1)
                s.add(point)
                stepsTo += 1
                if point not in lens:
                    lens[point] = stepsTo
        elif d == 'U':
            for i in range(l):
                point = (point[0], point[1] - 1)
                s.add(point)
                stepsTo += 1
                if point not in lens:
                    lens[point] = stepsTo

process(wire2, w2p, w2steps)
process(wire1, w1p, w1steps)

intersect = w1p & w2p



print("Part One : ", min(dist(p) for p in intersect))



print("Part Two : ", min(w1steps[p] + w2steps[p] for p in intersect))