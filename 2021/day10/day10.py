import sys

score = 0
scores = {
    ")": 3,
    "]: 57,
    "}": 1197,
    ">": 25137,
}
scores2 = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}
s2 = []
for line in sys.stdin.read().strip().splitlines():
    score2 = 0
    s = []
    for c in line.strip():
        if c in "(<[{":
            s.append(c)
        else:
            b = s.pop()
            if abs(ord(b) - ord(c)) > 3:
                score += scores[c]
                break
    else:
        while len(s):
            score2 *= 5
            score2 += scores2[s.pop()]
        s2.append(score2)
s2.sort()
print(score, s2[len(s2)//2])
