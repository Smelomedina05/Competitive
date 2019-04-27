###10687-Amazon UVa
###Santiago Melo Medina

from sys import stdin
from collections import deque
from math import *

def dfs(u):
    global G, visited
    visited[u] = 1
    for v in G[u]:
        if not visited[v]:
            dfs(v)

def graph(V):
    global G
    for u in range(len(V)):
        dist = sorted([(distance(V[u], V[v]), V[v][0], -1*V[v][1], v) for v in range(len(V)) if u != v])
        if 0 < len(dist): G[u].append(dist[0][3])
        if 1 < len(dist): G[u].append(dist[1][3])

def distance(first, second):
    x1, x2 = first[0], second[0]
    y1, y2 = first[1], second[1]
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def main():
    global G, visited
    c = deque(''.join(stdin.readlines()).split())
    while len(c):
        nodes = int(c.popleft())
        V = []
        G = [[] for n in range(nodes)]
        for n in range(nodes):
            V.append((int(c.popleft()), int(c.popleft())))
        if nodes:
            graph(V)
            visited = [0]*len(G)
            dfs(0)
            count = 0
            for n in visited: count += n
            if count == len(V): print("All stations are reachable.")
            else: print("There are stations that are unreachable.")

main()
