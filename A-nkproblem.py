from sys import stdin
from collections import deque
import sys

# FINISHED!
## Rocha TestCases Approved

## Divide and Conquer

""" Dado un k, se debe encontrar el minimo de numeros en una secuencia de 0,1,2,3,...,n en donde de como resultado k luego de operar
    cualquier posible combinacion los numeros de la secuencia con operadores '+' y '-'.
    testcase:
        12 -> 7 --->> -1+2+3+4+5+6-7 = 12"""

def upperBound(A, lw, hi, last):
    while lw < hi-1:
        middle = lw + ((hi-lw)//2)
        if A[middle] >= last:
            lw, hi = lw, middle
        else:
            lw, hi = middle, hi
    return hi

def problem(A, k, lw, hi, x):
    parity = k%2 == 0
    n = upperBound(A, 0, len(A)-1, k)
    while (not x(n+1)%2) != parity:
        n += 1
    return n+1

def main():
    cs = deque(''.join(stdin.readlines()).split())
    cs.popleft()
    A, s = [], 1
    x = lambda x : (x*(x+1))//2
    while x(s) < 10**10:
        A.append(x(s))
        s += 1
    while len(cs):
        k = int(cs.popleft())
        print(problem(A, abs(k), 0, x(k)-1, x))
        if len(cs): print()

main()
