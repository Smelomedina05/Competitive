from sys import stdin
from collections import deque

def bfs(n):
    global G, final, visited
    d = deque()
    d.append(n); visited[n] = 1
    while len(d):
        e = d.popleft()
        visited[e] = 1
        for s in G[e]:
            if n == s: final[s] += 2
            else: final[s] += 1
            if visited[s] == 0:
                d.append(s)

def count(num):
    zeros, dos, c = 0, 0, 0
    for n in num:
        if n == 0: zeros += 1
        elif n == 2: dos += 1
    return (zeros, dos, zeros+dos)

def main():
    global G, final, visited
    c = deque(''.join(stdin.readlines()).split())
    G, terms, temp, cs = [], [], [], 1
    while len(c):
        f, s = int(c.popleft()), int(c.popleft())
        if f or s:
            temp.append((f,s))
            if f not in terms:
                terms.append(f)
            if s not in terms:
                terms.append(s)
        else:
            G = [[] for n in range(len(terms))]
            final = [0]*len(G)
            visited = [0]*len(G)
            for n in temp:
                nodo, close = terms.index(n[0]), terms.index(n[1])
                G[nodo].append(close)

            for n in range(len(G)):
                if visited[n] == 0:
                    bfs(n)
            nums = count(final)
            if not nums[2]: print("Case {} is a tree.".format(cs))
            else:
                if nums[0] == 1 and not nums[1]: print("Case {} is a tree.".format(cs))
                else: print("Case {} is not a tree.".format(cs))
            G, terms, temp = [], [], []
            cs += 1

main()
