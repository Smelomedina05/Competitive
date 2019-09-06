from collections import deque
from sys import stdin

def binary(n):
    result = deque()
    while n:
        result.appendleft(0 if n%2 else 1)
        n //= 2
    return deque([1]*(33-len(result)))+result if len(result) < 33 else result

def bit(n, lw, hi, high):
    binn = binary(n)
    result = 0
    for bitn in range(len(binn)):
        tmp = 2**32 >> bitn
        if binn[bitn] and result+tmp <= hi:
            result += tmp
        elif not binn[bitn] and result+tmp <= lw:
            result += tmp
    return result

def main():
    cs = deque(''.join(stdin.readlines()).split())
    high = 2**32
    while len(cs):
        print(bit(int(cs.popleft()), int(cs.popleft()), int(cs.popleft()), high))
    return

main()
