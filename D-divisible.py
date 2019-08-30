from sys import stdin
from collections import deque
import sys

sys.setrecursionlimit(100000)

# FINISHED!
## Rocha TestCases Approved

## Divide and Conquer

""" La secuencia se puede operar alternando los simbolos de operacion '+' '-', el numero de alternaciones posibles es de 2**(n+1),
    n = numeros en la secuencia. De todos los posibles resultados, si existe uno que sea divisible por k, es divisible.
    testcase:
        (k = 7) 17 5 -21 15 -> Divisible --->> (17 + 5 + -21 - 15)%7 = 0"""

def divisible(A, n, k, acum):
    global memo
    key = "{}:{}".format(n, acum)
    if key in memo:
        result = memo[key]
    elif n >= len(A):
        result = not acum
    else:
        result = divisible(A, n+1, k, (acum+A[n])%k) or divisible(A, n+1, k, (acum-A[n])%k)
    memo[key] = result
    return result

def main():
    global memo, done
    cs = deque(''.join(stdin.readlines()).split())
    cs.popleft()
    while len(cs):
        n, k = int(cs.popleft()), int(cs.popleft())
        N = [int(cs.popleft()) for _ in range(n)]
        memo = {}
        print("Divisible" if divisible(N, 0, k, 0) else "Not divisible")

main()
