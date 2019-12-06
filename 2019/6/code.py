import functools

with open(__file__.rstrip('code.py') + 'input.txt', 'r') as (input_file):
    input = input_file.read().split('\n')

orbit = {}

for row in input:
    a, b = row.split(')')
    orbit[b] = a

@functools.lru_cache(maxsize=None)
def count_orbits(start):
    if start == 'COM':
        return 0
    return 1 + count_orbits(orbit[start])

print("Part 1 ", sum(count_orbits(o) for o in orbit.keys()))

costs = {
    orbit['YOU']: 0
}
target = orbit['SAN']

frontier = [orbit['YOU']]

while True:
    x = frontier.pop()

    if x == 'COM':
        continue

    if x == target:
        print('Part Two: ', costs[x])
        break
    else:
        for o, k in orbit.items():
            if k == x and (o not in costs or costs[x] + 1 < costs[o]):
                frontier.append(o)
                costs[o] = costs[x] + 1
        if orbit[x] not in costs or costs[x] + 1 < costs[orbit[x]]:
            frontier.append(orbit[x])
            costs[orbit[x]] = costs[x] + 1
