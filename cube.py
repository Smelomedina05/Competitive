from collections import deque
from sys import stdin

def yaxis(cube):
    return ''.join([cube[4], cube[0], cube[2], cube[3], cube[5], cube[1]])

def xaxis(cube):
    return ''.join([cube[0], cube[2], cube[4], cube[1], cube[3], cube[5]])

def zaxis(cube):
    return ''.join([cube[3], cube[1], cube[0], cube[5], cube[4], cube[2]])

def main():
    c = deque(''.join(stdin.readlines()).split())
    while len(c):
        cube = c.popleft()
        start, end = cube[0:6], cube[6:len(cube)]
        found = False
        for n in range(4):
            start = yaxis(start)
            for m in range(4):
                start = xaxis(start)
                for s in range(4):
                    start = zaxis(start)
                    if start == end: found = True
        print("TRUE" if found else "FALSE")


main()
