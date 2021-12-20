data = open(0).readlines()

e = [i == "#" for i in data[0].strip()]
b = [line.strip() for line in data[2:]]
d = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1))
def neighbors(i, j):
    for k, (di, dj) in enumerate(d):
        yield 256 >> k, i+di, j+dj
def lookup(_s, i, j, bi, bj, flip=False):
    if i == bi[0] or i + 1 == bi[1] or j == bj[0] or j + 1 == bj[1]:
        return ((i, j) in _s) ^ flip
    return e[sum(k for k, ni, nj in neighbors(i, j) if (ni, nj) in _s)]
s = frozenset((i, j) for i in range(len(b)) for j in range(len(b[0])) if b[i][j] == "#")
bi = (-51, len(b)+51)
bj = (-51, len(b[0])+51)
def iterate(_s, bi, bj):
    return frozenset((i, j) for i in range(*bi) for j in range(*bj) if lookup(_s, i, j, bi, bj, e[0]))
for _ in range(2):
    s = iterate(s, bi, bj)
print("Part 1", len(s))
for _ in range(48):
    s = iterate(s, bi, bj)
print("Part 2", len(s))

for i in range(*bi):
    for j in range(*bj):
        if (i, j) in s:
            print("#", end="")
        else:
            print(".", end="")
    print()