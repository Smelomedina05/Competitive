###10009-Allroads
### Santiago Melo Medina 2019-1

from collections import deque
from sys import stdin

def extra(u, s, found):
    global parents, VN
    path = deque()
    while u != parents[u]:
        path.appendleft(VN[u])
        u = parents[u]
    path.appendleft(VN[u])
    print(''.join([n[0] for n in path]))

def bfs(s, e):
    global G, parents
    visited = [0]*len(G)
    parents = [n for n in range(len(G))]
    d = deque()
    d.append(s)
    found = False
    while len(d) and not found:
        u = d.popleft()
        visited[u] = 1
        if u == e: found = True
        else:
            for v in G[u]:
                if not visited[v]:
                    parents[v] = u
                    d.append(v)
    extra(u, s, found)
    return




def main():
    global G, VN
    c = deque(''.join(stdin.readlines()).split())
    css = int(c.popleft())
    for cs in range(css):
        edges, paths = int(c.popleft()), int(c.popleft())
        G = []
        NV, VN = {}, {}
        count = 0
        for n in range(edges):
            u, v = c.popleft(), c.popleft()
            if u not in NV:
                NV[u] = count
                VN[count] = u
                count += 1; G.append([])
            if v not in NV:
                NV[v] = count
                VN[count] = v
                count += 1; G.append([])
            u, v = NV[u], NV[v]
            G[u].append(v); G[v].append(u)
        for n in range(paths):
            bfs(NV[c.popleft()], NV[c.popleft()])
        if cs < css-1: print('')

main()
