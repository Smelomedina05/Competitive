from collections import deque
from sys import stdin

class SegmentTree:
    def __init__(self, A):
        hojas = 1
        while hojas < len(A): hojas*=2
        self.tree = [0 for n in range(2*hojas)]
        for n in range(len(A)):
            self.tree[n+hojas] = A[n]
        for n in range(hojas-1, 0, -1):
            self.tree[n] = self.tree[2*n]+self.tree[2*n+1]
        self.hojas = hojas
        return

    def suma(self, lo, hi):
        return self.aux_sum(lo,hi,1, 0, self.hojas) if len(self.tree) else 0

    def aux_sum(self, lo,hi,n, L, R):
        assert L<=lo<hi<=R
        middle = L + ((R-L)//2)
        if L == lo and R==hi:
            result = self.tree[n]
        elif hi <= middle:
            result = self.aux_sum(lo, hi, 2*n, L, middle)
        elif lo >= middle:
            result = self.aux_sum(lo, hi, 2*n+1, middle, R)
        else:
            result = self.aux_sum(lo, middle, 2*n, L, middle)
            result += self.aux_sum(middle, hi, 2*n+1, middle, R)
        return result

    def set(self, n, value):
        n = n+self.hojas
        self.tree[n] = value
        while n!=1:
            n//=2
            self.tree[n] = self.tree[2*n]+self.tree[2*n+1]
        return

    def get(self, n):
        return self.tree[self.hojas-1+n]

def main():
    c = deque(''.join(stdin.readlines()).split())
    cs = 1
    if len(c): pots = int(c.popleft())
    while len(c):
        if pots:
            print("Case {}:".format(cs))
            A = [int(c.popleft()) for n in range(pots)]
            s = SegmentTree(A)
            ins = c.popleft()
            while ins != "END":
                data = [int(c.popleft()), int(c.popleft())]
                if ins == 'M':
                    data = sorted(data)
                    if data[0] != data[1]: print(s.suma(data[0]-1, data[1]))
                    else: print(s.get(data[0]))
                else:
                    s.set(data[0]-1, data[1])
                ins = c.popleft()
        pots = int(c.popleft())
        if pots: print('')
        cs += 1

main()
