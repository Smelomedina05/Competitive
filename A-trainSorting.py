from sys import stdin
from collections import deque

## Hopefully finished

### Lis and lds

def lis(A):
    result = [1 for _ in range(len(A))]
    for n in range(1, len(A)):
        for s in range(n):
            if A[n] > A[s]:
                result[n] = max(result[n], result[s]+1)
    return result

def lds(A):
    result = [1 for _ in range(len(A))]
    for n in range(1, len(A)):
        for s in range(n):
            if A[n] < A[s]:
                result[n] = max(result[n], result[s]+1)
    return result

def interface(A):
    increasing = lis(A)
    decreasing = lds(A)
    result = 0
    for n in range(len(increasing)):
        result = max(result, increasing[n]+decreasing[n]-1)
    return result

def main():
    cs = deque(''.join(stdin.readlines()).split())
    cs.popleft()
    while len(cs):
        A = [int(cs.popleft()) for _ in range(int(cs.popleft()))]
        print(interface(A[::-1]))
    return

main()
