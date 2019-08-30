from collections import deque
from sys import stdin

def kmpPre(P):
    i, j = 0, -1
    f = [-1 for n in range(len(P)+1)]
    while i < len(P):
        while j >= 0 and P[i]!=P[j]: j = f[j]
        i += 1
        j += 1
        f[i] = j
    return f

def main():
    c = deque(''.join(stdin.readlines()).split())
    c.popleft()
    while len(c):
        word = c.popleft()
        f = kmpPre(word+word[::-1])
        f = f[::-1]
        f = f[0:len(word)]
        great, last = float("-inf"), 0
        for n in range(len(f)):
            if f[n] > great:
                great = f[n]
                last = n
        print(word[last:last+great])

main()
