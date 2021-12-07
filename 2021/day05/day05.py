with open("input.txt", "r") as f:
    points = [[int(x) for k in line.strip().split(" -> ") for x in k.split(",")] for line in f.readlines()]

# Please remember to use Counter next time...
covered = {}
for l in fpoints:
    for x in range(min(l[0], l[2]), max(l[0], l[2])+1):
        for y in range(min(l[1], l[3]), max(l[1], l[3])+1):
            if f"{x},{y}" in covered:
                covered[f"{x},{y}"] += 1
            else:
                covered[f"{x},{y}"] = 1

print("Part 1", sum(1 for i in covered.values() if i > 1))

for l in dpoints:
    d1 = int(l[2] > l[0]) or -1
    d2 = int(l[3] > l[1]) or -1
    for i in range(abs(l[2] - l[0]) + 1):
        x = l[0] + d1 * i
        y = l[1] + d2 * i
        if f"{x},{y}" in covered:
            covered[f"{x},{y}"] += 1
        else:
            covered[f"{x},{y}"] = 1

print("Part 2", sum(1 for i in covered.values() if i > 1))