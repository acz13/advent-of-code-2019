def part1(pos):
    return int(min(sum(abs(i - k) for k in pos) for i in range(1, max(pos)+1)))

def part2(pos):
    return int(min(sum(abs(i - k)*(abs(i - k)+1)/2 for k in pos) for i in range(1, max(pos)+1)))

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split(",")]
    print("Part 1:", part1(pos))
    print("Part 2:", part2(pos))
