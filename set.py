from collections import deque
from sys import stdin

def johnson(A, B):
    left, right = [], []
    for n in range(len(A)):
        left.append((A[n], B[n])) if A[n] < B[n] else right.append((A[n], B[n]))
    left = sorted(left, key = lambda x : x[0])
    right = sorted(right, key = lambda x : x[1], reverse=True)
    ta, tb = 0, 0
    for n in left+right:
        ta += n[0]
        tb = max(ta, tb)+n[1]
    return tb

def main():
    cs = deque(''.join(stdin.readlines()).split())
    while len(cs):
        n = int(cs.popleft())
        print(johnson([int(cs.popleft()) for _ in range(n)], [int(cs.popleft()) for _ in range(n)]))
    return

main()
