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
            self.tree[n] = self.tree[2*n]*self.tree[2*n+1] #Product instead of addition
        self.hojas = hojas
        return

    def product(self, lo, hi):
        return self.aux_product(lo,hi,1, 0, self.hojas) if len(self.tree) else 0

    def aux_product(self, lo,hi,n, L, R):
        assert L<=lo<hi<=R
        middle = L + ((R-L)//2)
        if L == lo and R==hi:
            result = self.tree[n]
        elif hi <= middle:
            result = self.aux_product(lo, hi, 2*n, L, middle)
        elif lo >= middle:
            result = self.aux_product(lo, hi, 2*n+1, middle, R)
        else:
            result = self.aux_product(lo, middle, 2*n, L, middle)
            result *= self.aux_product(middle, hi, 2*n+1, middle, R) ##Change here
        return result

    def set(self, n, value):
        n = n+self.hojas
        self.tree[n] = value
        while n!=1:
            n//=2
            self.tree[n] = self.tree[2*n]*self.tree[2*n+1] ##Change here
        return

    def get(self, n):
        return self.tree[self.hojas-1+n]

def main():
    c = deque(''.join(stdin.readlines()).split())
    while len(c):
        hojas, inss = int(c.popleft()), int(c.popleft())
        A = [int(c.popleft()) for n in range(hojas)]
        s = SegmentTree(A)
        for n in range(inss):
            ins, data = c.popleft(), [int(c.popleft()), int(c.popleft())]
            if ins == 'P':
                producto = s.product(data[0]-1, data[1])
                parcial = ''
                if producto > 0: parcial = '+'
                elif producto < 0: parcial = '-'
                else: parcial = '0'
                print(parcial, end="")
            else: s.set(data[0]-1, data[1])
        print('')

main()
