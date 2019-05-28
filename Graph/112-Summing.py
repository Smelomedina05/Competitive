from sys import stdin
import sys
from collections import deque

sys.setrecursionlimit(10000)

def arbol(t, acum, num):
    global n, result
    while n < len(t) and not t[n].isdigit() and t[n] != '-':
        n += 1
    m = n + 1
    while m < len(t) and t[m].isdigit():
        m += 1
    val = int(t[n:m])
    n = m
    if m < len(t) and t[m] == '(':
        n += 1
        x = arbol(t, acum + val, num)
        n += 2
        y = arbol(t, acum + val, num)
        if acum+val == num and not len(x) and not len(y): result = True
        tree = [val, x, y, val + acum]
    else:
        if val == 0:
            tree = []
        else:
            tree = [val]
    return tree


def use(t):
    global n, result
    n = 0
    result = False
    count = 0
    while count < len(t) and (t[count].isdigit() or t[count] == '-'):
        count += 1
    num = int(t[0:count])
    arbol(t[count+1:][:-1], 0, num)
    print("yes" if result else "no")

def main():
    c = ''.join((''.join(stdin.readlines())).split())
    c = deque([n for n in c])
    tree, last = "", ''
    while len(c):
        e = c.popleft()
        if last == ')' and (e.isdigit() or e=='-'):
            use(tree)
            c.appendleft(e)
            tree, last = "", ''
        elif last == '(' and e == ')':
            tree += "0)"
            last = e
        else:
            tree += e
            last = e
    use(tree)

main()
