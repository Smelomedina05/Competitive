from sys import stdin
from collections import deque

# FINISHED!
## Rocha TestCases Approved

## Divide and Conquer

def lowerBound(A, lw, hi, last):
    while lw < hi-1:
        middle = lw + ((hi-lw)//2)
        if A[middle] > last:
            lw, hi = lw, middle
        else:
            lw, hi = middle, hi
    if A[lw] > last:
        result = True, A[lw]
    elif A[hi] > last:
        result = True, A[hi]
    else:
        result = False, None
    return result

def helping():
    global S, s
    fine = True
    n, last = 0, -1
    lasts = []
    while n < len(s) and fine:
        ref = ord(s[n])-65 if ord(s[n]) <= 90 else ord(s[n])-71
        if len(S[ref]):
            fine, last = lowerBound(S[ref], 0, len(S[ref])-1, last)
            lasts.append(last)
        else:
            fine = False
        n += 1
    return lasts, fine

def main():
    global S, s
    cs = deque(''.join(stdin.readlines()).split())
    tmp = cs.popleft()
    S = [[] for _ in range(52)]
    for c in range(len(tmp)):
        ref = ord(tmp[c])-65 if ord(tmp[c]) <= 90 else ord(tmp[c])-71
        S[ref].append(c)
    cs.popleft()
    while len(cs):
        s = cs.popleft()
        result = helping()
        print("Not matched" if not result[1] else "Matched {} {}".format(result[0][0], result[0][-1]))

main()
