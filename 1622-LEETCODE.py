class Fancy:

    def __init__(self):
        self.M = 10**9 + 7
        self.seq = []
        self.add = 0
        self.mult = 1

    def append(self, val: int) -> None:
        x = ((val - self.add) % self.M) * pow(self.mult, self.M - 2, self.M) % self.M
        self.seq.append(x)

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.M

    def multAll(self, m: int) -> None:
        self.mult = (self.mult * m) % self.M
        self.add = (self.add * m) % self.M

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mult + self.add) % self.M
