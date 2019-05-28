from collections import deque
from sys import stdin

def bfs(start, end, grafo, freezed, visited):
    d = deque()
    d.append((start, 0))
    found = False
    result = 0
    for n in freezed:
        visited[n] = 1
    while len(d) and not found:
        item = d.popleft()
        if item[0] == end: found = True
        else:
            for n in grafo[item[0]]:
                if visited[n] == 0:
                    d.append((n, item[1]+1))
                    visited[n] = 1
    if found: result = item[1]
    else: result = -1
    return result


def sig(n):
    r = n + 1
    if n == 9:
        r = 0
    return r

def ant(n):
    r = n - 1
    if n == 0:
        r = 9
    return r

def getNum(num):
    return num[0]*1000+num[1]*100+num[2]*10+num[3]

def perm():
    total, visited = [], []
    c = 0
    for n in range(10):
        for m in range(10):
            for s in range(10):
                for r in range(10):
                    total.append([])
                    total[c].append(getNum((n,m,s,sig(r))))
                    total[c].append(getNum((n,m,s,ant(r))))
                    total[c].append(getNum((n,m,sig(s),r)))
                    total[c].append(getNum((n,m,ant(s),r)))
                    total[c].append(getNum((n,sig(m),s,r)))
                    total[c].append(getNum((n,ant(m),s,r)))
                    total[c].append(getNum((sig(n),m,s,r)))
                    total[c].append(getNum((ant(n),m,s,r)))
                    c += 1
    return total

def main():
    w = ''.join(stdin.readlines()).split()
    c = deque(w)
    listan = perm()
    visited = [0]*len(listan)
    for n in range(int(c.popleft())):
        freezed = []
        start = getNum((int(c.popleft()), int(c.popleft()), int(c.popleft()), int(c.popleft())))
        end = getNum(((int(c.popleft()), int(c.popleft()), int(c.popleft()), int(c.popleft()))))
        for m in range(int(c.popleft())):
            freezed.append(getNum((int(c.popleft()), int(c.popleft()), int(c.popleft()), int(c.popleft()))))
        print(bfs(start, end, listan, freezed, visited[:]))

main()
