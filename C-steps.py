from sys import stdin
from collections import deque

# FINISHED!
## Rocha TestCases Approved

## Divide and Conquer

""" Se da dos niveles x y y, hay que llegar de x a y en minimo de pasos en donde un paso puede ser un numero entre el numero
    de pasos recorridos mas 1, el ultimo paso y el primer paso deben ser 1.
    testcase:
        45 48 -> 3 --->> 1, 1, 1
        45 49 -> 3 --->> 1, 2, 1
        45 50 -> 4 --->> 1, 2, 2, 1"""

def lowerBound(lw, hi, k, f):
    while lw < hi-1:
        middle = lw + ((hi-lw)//2)
        if f(middle) <= k:
            lw = middle
        else:
            hi = middle
    return lw

def steps(x, y, f):
    result = lowerBound(0, 2**31, y-x, f)
    falta = y-x-f(result)
    extra = 0
    if falta:
        if result+1 < falta: extra = 2
        else: extra = 1
    return 2*(result)+extra

def main():
    cs = deque(''.join(stdin.readlines()).split())
    cs.popleft()
    while len(cs):
        x, y = int(cs.popleft()), int(cs.popleft())
        f = lambda n : n*(n+1)
        print(steps(x,y,f))

main()
