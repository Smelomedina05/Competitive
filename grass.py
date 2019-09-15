from sys import stdin
from collections import deque
import math

def intervalCovering(A, l):
    A = sorted(A)
    ancker, i = 0, 0
    count, hole = 0, 0
    while i < len(A) and ancker < l and not hole:
        hole = A[i][0] > ancker
        longest = i
        i += 1
        while  i < len(A) and A[i][0] <= ancker:
            if A[i][1] > A[longest][1]:
                longest = i
            i += 1
        ancker = A[longest][1]
        count += 1
    return count if not hole and ancker >= l else -1

def main():
    cs = deque(''.join(stdin.readlines()).split())
    f = lambda x, y : math.sqrt(x**2 - (y/2)**2) if x**2 - (y/2)**2 > 0 else None
    while len(cs):
        n, l, w = int(cs.popleft()), int(cs.popleft()), int(cs.popleft())
        A = []
        for _ in range(n):
            p, r = int(cs.popleft()), int(cs.popleft())
            tmp = f(r, w)
            if tmp != None: A.append((p-tmp, p+tmp))
        print(intervalCovering(A, l))
    return

main()
