from points import Point, double_rotations, rotations
from itertools import combinations

scanners = []
offset = None
scanner = None
for line in open("input.txt").readlines():
    if line.startswith("---"):
        scanner = []
        scanners.append(scanner)
    elif len(line) > 1:
        scanner.append(eval("Point("+line.strip()+")"))

def position(s1, s2):
    s1s = set(s1)
    for i in range(len(s1)-11):
        s1o = s1[i]
        for j in range(len(s2)-11):
            s2o = s2[j]
            for ri, r in enumerate(rotations):
                _s2os = set(s1o + r(p - s2o) for p in s2)
                if len(s1s & _s2os) >= 12:
                    return ri, s1o - r(s2o), (s1s | _s2os)

positions = {
    0: (11, Point(0, 0, 0))
}

beacons = set(scanners[0])
to_test = [0]
while len(scanners) > len(positions):
    newly_added = []
    for s in range(len(scanners)):
        if s not in positions:
            for _s in to_test:
                r = position(scanners[_s], scanners[s])
                base_r, base_p = positions[_s]
                if r is not None:
                    rotation, pos, points = r
                    dr = double_rotations[rotation][base_r]
                    beacons.update(base_p + p.rotate(base_r) for p in points)
                    print(s, _s, len(beacons))
                    positions[s] = (dr, base_p + pos.rotate(base_r))
                    newly_added.append(s)
                    break
    to_test = newly_added

print("Part 1", len(beacons))
print("Part 2", max((positions[s][1] - positions[_s][1]).total() for s, _s in combinations(positions, 2)))
