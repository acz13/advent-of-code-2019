f = open("input.txt", "r").readlines()
u = 0
c = [1] * len(f)
for i, l in enumerate(f):
    s = l.split()
    w = set(map(int, s[2:12]))
    m = list(map(int, s[13:]))
    k = sum(1 for i in m if i in w)
    for j in range(k):
        c[j + 1 + i] += 1 * c[i]
    if k:
        u += 1<<(k-1)
print(u)
print(sum(c))
