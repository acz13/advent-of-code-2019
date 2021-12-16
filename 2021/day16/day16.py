import operator
import functools

lines = list(open(0))

def i(s):
    return int(s, 2)
def b(n):
    return f"{n:b}"

class Parser():
    def __init__(self, line, p=0, depth=0):
        self.line = line
        self.p = p
        self.depth = depth
        self.tV = 0
    
    def rb(self, l):
        b = self.line[self.p:self.p+l]
        self.p += l
        return b

    def ri(self, l):
        return i(self.rb(l))

    def print(self, *args, **kwargs):
        print("  "*self.depth, *args, **kwargs)
        pass

    @staticmethod
    def out(T, s):
        if T == 0:
            return sum(s)
        elif T == 1:
            return functools.reduce(operator.mul, s)
        elif T == 2:
            return min(s)
        elif T == 3:
            return max(s)
        elif T == 5:
            assert len(s) == 2
            return int(s[0] > s[1])
        elif T == 6:
            assert len(s) == 2
            return int(s[0] < s[1])
        elif T == 7:
            assert len(s) == 2
            return int(s[0] == s[1])

    def parse(self):
        self.print("Starting p", self.p, "out of", len(self.line))
        V = self.ri(3)
        self.tV += V
        T = self.ri(3)
        self.print("Version", V, "Type", T)
        if T == 4:
            # literal
            lv = ""
            while self.ri(1) == 1:
                lv += self.rb(4)
            lv += self.rb(4)
            vv = i(lv)
            self.print("Literal value", vv)
            return vv
        else:
            ol = [15, 11][self.ri(1)]
            ll = self.ri(ol)
            self.print("Subpacket", ol, ll)
            s = []
            c = 0
            while c < ll:
                subP = Parser(self.line, p=self.p, depth=self.depth+1)
                s.append(subP.parse())
                self.tV += subP.tV
                if ol == 15:
                    c += subP.p - self.p
                elif ol == 11:
                    c += 1
                self.p = subP.p
            ret = Parser.out(T, s)
            self.print("Operator value", ret)
            return ret


for line in lines:
    binary = ""
    for c in line.strip().split()[0]:
        binary += f"{int(c, 16):b}".zfill(4)
    print(line.strip())
    P = Parser(binary)
    r = P.parse()
    print("Part 1", P.tV)
    print("Part 2", r)
    print()

