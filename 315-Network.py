from sys import stdin
from collections import deque

def tarjan(G):
    global depth, low, criticos, parents
    criticos = set()
    n = len(G)
    parents = [-1 for m in range(n)]
    depth, low = [-1 for m in range(n)], [-1 for m in range(n)]
    for u in range(n):
        if depth[u] == -1:
            depth[u] = low[u] = 0
            dfs(u, G)
    return

def dfs(u, G):
    recorridos = 0
    for v in G[u]:
        if depth[v] == -1: #Si no lo he visitado, es un tree-edge
            depth[v] = low[v] = depth[u]+1
            parents[v] = u
            recorridos += 1
            dfs(v, G)
            low[u] = min(low[u], low[v])
            if parents[u] == -1:
                if recorridos > 1: criticos.add(u)
            elif depth[u] <= low[v]: criticos.add(u)
        else: # Back-edge
            low[u] = min(low[u], depth[v])
    return

def main():
    c = stdin.readlines()
    c = deque(c)
    while len(c):
        cs = int(c.popleft().strip())
        graph = [[] for n in range(cs)]
        end = False
        while cs and not end:
            nd = list(map(int, c.popleft().split()))
            if not nd[0]: end = True
            else:
                graph[nd[0]-1] += [n-1 for n in nd[1:]]
                for m in nd[1:]:
                    graph[m-1].append(nd[0]-1)
            cs -= 1
        if len(graph):
            tarjan(graph)
            print(len(criticos))

main()
