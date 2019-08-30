from sys import stdin
from collections import deque

def change(A, q):
    maximo = 20000
    dp = [len(A)+1 for _ in range(maximo+2)]
    dp[0] = 0
    first = [0, True]
    for coin in A:
        first[1] = True
        for n in range(first[0], -1, -1):
            if n+coin <= maximo:
                dp[n+coin] = min(dp[n+coin], dp[n]+1)
                if first[1]:
                    first[1] = False
                    first[0] = n+coin
    n, found = q, float("-inf")
    while n <= maximo+1 and found == float("-inf"):
        if dp[n] < len(A)+1:
            found = dp[n]
        n += 1
    return found, n-1


def main():
    cs = deque(''.join(stdin.readlines()).split())
    cs.popleft()
    while len(cs):
        q, c = int(cs.popleft()), int(cs.popleft())
        coins = [int(cs.popleft()) for _ in range(c)]
        result = change(coins, q)
        print("{} {}".format(result[1], result[0]))
    return

main()
