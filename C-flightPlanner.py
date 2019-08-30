
from sys import stdin
from collections import deque

def flight(A):
    dp = [[float("inf") for _ in range(len(A[0])+1)] for _ in range(len(A))]
    dp[-1][0] = 0
    for col in range(1, len(dp[0])):
        for row in range(len(dp)-1, -1, -1):
            for v, s in [(20, 1), (30, 0), (60, -1)]:
                if row+s <= 9 and row+s >= 0:
                    dp[row][col] = min(dp[row][col], dp[row+s][col-1]+v-A[row+s][col-1])
    return dp[-1][-1]

def main():
    cs = deque(''.join(stdin.readlines()).split())
    cs.popleft()
    while len(cs):
        N = int(cs.popleft())
        A = [[int(cs.popleft()) for _ in range(N//100)] for _ in range(10)]
        print(flight(A))
        print()
    return

main()
