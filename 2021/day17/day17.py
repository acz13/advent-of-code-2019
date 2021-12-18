class Probe:
    def __init__(self, vx, vy, x, y):
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.vx != 0:
            self.vx -= self.vx // abs(self.vx)
        self.vy -= 1

    def contained(self, x1, x2, y1, y2):
        return self.x >= x1 and self.x <= x2 and self.y >= y1 and self.y <= y2

    def reachable(self, x1, x2, y1, y2):
        return self.x <= x2 and ((self.y <= y2 and self.vy > -1) or self.y >= y1)  

target = (175,227, -134,-79)

o = []
def test(vx, vy, part2):
    p = Probe(vx, vy, 0, 0)
    ys = []
    while p.reachable(*target):
        p.update()
        ys.append(p.y)
        if p.contained(*target):
            o.append([vx, vy])
            return 1 if part2 else max(ys)
    return 0

print("Part 1", max(test(i, j, False) for i in range(0, 304) for j in range(-200, 200)))
print("Part 2", sum(test(i, j, True) for i in range(0, 304) for j in range(-200, 200)))

xs, ys = zip(*o)
print(min(xs), max(xs))
print(min(ys), max(ys))