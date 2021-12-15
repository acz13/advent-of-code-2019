import heapq as hq

class Graph:
    def neighbors(self, node):
        raise NotImplementedError()

    def cost(self, current, neighbor):
        raise NotImplementedError()

    def heuristic(self, node, goal):
        raise NotImplementedError()

class ChitonGrid(Graph):
    def __init__(self, grid):
        self.grid = [list(map(int, l)) for l in grid.strip().splitlines()]
        self._y = len(self.grid)
        self._x = len(self.grid[0])
        self.part2 = False

    @property
    def x(self):
        if self.part2:
            return self._x * 5
        else:
            return self._x

    @property
    def y(self):
        if self.part2:
            return self._y * 5
        else:
            return self._y

    def __getitem__(self, i):
        y, x = i
        if self.part2:
            return ((self.grid[y % self._y][x % self._x] + y // self._y + x // self._x) - 1) % 9 + 1
        else:
            return self.grid[y][x]

    def neighbors(self, node):
        if node[0] > 0:
            yield node[0] - 1, node[1]
        if node[0] + 1 < self.y:
            yield node[0] + 1, node[1]
        if node[1] > 0:
            yield node[0], node[1] - 1
        if node[1] + 1 < self.y:
            yield node[0], node[1] + 1

    def cost(self, current, neighbor):
        return self[neighbor]

    def heuristic(self, node, goal):
        return abs(goal[0] - node[0]) + abs(goal[1] - node[1])

def astar(graph, start, goal):
    parents = { start: (0, None) }
    frontier = []
    hq.heappush(frontier, (graph.heuristic(start, goal), start))
    while len(frontier):
        _, node = hq.heappop(frontier)
        cost = parents[node][0]
        if node == goal:
            path = [node]
            while node != start:
                path.append((node := parents[node][1]))
            return reversed(path)
        for neighbor in graph.neighbors(node):
            cost_ = cost + graph.cost(node, neighbor)
            if neighbor not in parents or cost_ < parents[neighbor][0]:
                parents[neighbor] = (cost_, node)
                hq.heappush(frontier, (cost_ + graph.heuristic(neighbor, goal), neighbor))

g = ChitonGrid(open(0).read())
print(sum(g[i] for i in astar(g, (0, 0), (g.y-1, g.x-1))) - g[(0, 0)])
g.part2 = True
print(sum(g[i] for i in astar(g, (0, 0), (g.y-1, g.x-1))) - g[(0, 0)])
