from collections import deque
from sys import stdin

# FINISHED!

def maxPro(A):
    AR = A[::-1]
    for n in range(1, len(A)):
        A[n] *= A[n-1] if A[n-1] else 1
        AR[n] *= AR[n-1] if AR[n-1] else 1
    A += AR
    return max(A)

def main():
    cs = deque(''.join(stdin.readlines()).split())
    while len(cs):
        nums = []
        tmp = int(cs.popleft())
        while tmp != -999999:
            nums.append(tmp)
            tmp = int(cs.popleft())
        print(maxPro(nums))
    return

main()
