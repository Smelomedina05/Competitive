from collections import deque
from sys import stdin

def tarjan():
    global G, depth, low, parents, art
    depth = [-1]*len(G)
    low = [-1]*len(G)
    parents = [-1]*len(G)
    art = set()
    for u in range(len(G)):
        if depth[u] == -1:
            depth[u] = low[u] = 0
            dfs(u)
    return art

def dfs(u):
    global G, depth, low, parents, art
    children = 0
    for v in G[u]:
        if depth[v] == -1:
            children += 1
            depth[v] = low[v] = depth[u]+1
            parents[v] = u
            dfs(v)
            low[u] = min(low[u], low[v])
            if (parents[u] == -1 and children > 1) or (parents[u] != -1 and low[v]>=depth[u]):
                art.add(u)
        elif parents[u] != v:
            low[u] = min(low[u], depth[v])


def main():
    global G
    c = deque(''.join(stdin.readlines()).split())
    case = 1
    while len(c):
        cities = int(c.popleft())
        if cities:
            if case != 1: print('')
            citys, ncitys = {}, {}
            G = [[] for n in range(cities)]
            for n in range(cities):
                ciudad = c.popleft()
                citys[ciudad] = n
                ncitys[n] = ciudad
            for n in range(int(c.popleft())):
                c1, c2 = c.popleft(), c.popleft()
                G[citys[c1]].append(citys[c2])
                G[citys[c2]].append(citys[c1])
            points = tarjan()
            print("City map #{}: {} camera(s) found".format(case, len(points)))
            cts = sorted([ncitys[n] for n in points])
            if len(cts): print('\n'.join(cts))
            case += 1


main()
