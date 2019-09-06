from collections import deque
from sys import stdin

def f(n):
    count = 0
    while n:
        if n != 3:
            if not n%2:
                n //=2
            elif not ((n+1)//2)%2:
                n += 1
            else:
                n -= 1
            count += 1
        else:
            n-=1
            count += 1
    return count

def main():
    cs = deque(''.join(stdin.readlines()).split())
    while len(cs):
        print(f(int(cs.popleft())))
    return

main()
