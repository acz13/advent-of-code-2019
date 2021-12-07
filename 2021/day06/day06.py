import collections

def disp(i):
    s = str(i)
    return f"{s[0]}.{s[1:5]}e{len(s)-1}"

def lanternfish_count(ages, t):
    day_counter = collections.Counter(t - age - 1 for age in ages)

    # Start computing our table from here
    combs = collections.deque([1, 0, 0, 0, 0, 0, 0, 1, 0])
    # and our sums from here
    population = 3

    def _iterate():
        s = combs.popleft() + combs[1]
        combs.append(s)
        return s
    
    k = 8
    for i in range(9, t-6):
        population += _iterate()
        k += 1
        if k == 10000:
            print(f"\rDay {i}: Table at {disp(population)}", end="")
            k = 0
    
    count = 0

    for day in range(t-6, t):
        population += _iterate()
        count += day_counter[day] * population

    return count

if __name__ == "__main__":
    ages = [int(i) for i in input().strip().split(",")]
    print("Part 1:", lanternfish_count(ages, 80))
    print("Part 2:", lanternfish_count(ages, 256))
