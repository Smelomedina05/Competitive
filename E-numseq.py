from sys import stdin
from collections import deque

# FINISHED!
## Rocha TestCases Approved

## Divide and Conquer

""" Con la secuencia 112123123412345123456123456712345678... encontrar el numero en el indice n
    testcase:
        8 -> 2 --->> 1121231 - 2 (posicion 8) - 341
        3 -> 2 --->> 11 - 2 (posicion 3) - 123
    """

def lowerBound(A, lw, hi, n):
    found = False
    while lw < hi-1:
        middle = lw + ((hi-lw)//2)
        if A[middle] >= n:
            if A[middle] == n: found = True
            lw, hi = lw, middle
        else:
            lw, hi = middle, hi
    return n-A[lw] if not found else 0

def seq():
    A = [1]
    s, last, lasts = 1, 1, "1"
    while s <= 2147483648:
        s = A[-1]+len(lasts)
        A.append(s)
        last += 1
        lasts += str(last)
    return A, lasts

def main():
    cs = deque(''.join(stdin.readlines()).split())
    cs.popleft()
    A, S = seq()
    while len(cs):
        n = int(cs.popleft())
        result = lowerBound(A, 0, len(A)-1, n)
        print(S[result])

main()
