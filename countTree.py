from collections import deque
from sys import stdin
import math

def catalan(n):
    global memo
    result = 0
    if memo[n] != None:
        return memo[n]
    if n == 0 or n == 1:
        result = 1
    else:
        for s in range(1, n+1):
            result += catalan(s-1)*catalan(n-s)
    memo[n] = result
    return result

def main():
    global memo
    c = deque(''.join(stdin.readlines()).split())
    while len(c):
        n = int(c.popleft())
        memo = [None for _ in range(n+1)]
        if n: print(math.factorial(n)*catalan(n))

main()
