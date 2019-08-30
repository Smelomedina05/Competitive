from sys import stdin
from collections import deque

## Using disjoint sets and SCC we find whether there is only one stronghly connected components, after changing the graph by grouping the K nodes.
## Also it must be asure that all of the nodes form this one group.

def find(n):
    global parents
    if n == parents[n]:
        result = n
    else:
        result = find(parents[n])
        parents[n] = result
    return result


def tarjan():
    global G, depth, low, visited, scc, scctmp, num_components, parents
    depth = [-1]*len(G)
    low = [-1]*len(G)
    visited = [0]*len(G)
    scc, scctmp = [], deque()
    num_components = 0
    for u in range(len(G)):
        if depth[u] == -1:
            dfs(u)
    return scc

def dfs(u):
    global G, depth, low, visited, scc, scctmp, num_components, parents
    depth[u] = low[u] = num_components
    num_components += 1
    visited[u] = 1
    scctmp.append(u)
    for v in G[u]:
        if depth[v] == -1:
            dfs(v)
            low[u] = min(low[u], low[v])
        elif visited[v]:
            low[u] = min(low[u], depth[v])
    if (low[u]==depth[u]):
        s = scctmp.pop()
        tmp = []
        while s != u:
            tmp.append(s)
            s = scctmp.pop()
        tmp.append(s)
        scc.append(tmp)


def main():
    global parents, G
    cs = deque(''.join(stdin.readlines()).split())
    while len(cs):
        nodes = int(cs.popleft())
        p, num, dif, pp, count = {}, {}, {}, set(), 0
        parents = [s for s in range(nodes)]
        G, A = [], []
        for _ in range(int(cs.popleft())):
            n = int(cs.popleft())
            if n == 1:
                u, v = int(cs.popleft())-1, int(cs.popleft())-1
                A.append((u, v))
            else:
                current = int(cs.popleft())-1
                for _ in range(n-1):
                    tmp = int(cs.popleft())-1
                    parents[find(tmp)] = find(current)
                    current = tmp
        for n in range(len(parents)): find(n)
        for parent in parents:
            pp.add(parent)
            if parent not in dif: dif[parent] = 1
            else: dif[parent] += 1
        for u, v in A:
            u, v = find(u), find(v)
            if u not in p:
                p[u] = count
                num[count] = u
                count += 1
                G.append([])
            if v not in p:
                p[v] = count
                num[count] = v
                count += 1
                G.append([])
            G[p[u]].append(p[v])
        result = tarjan()
        if (len(result) == 0 and len(pp) == 1) or (len(result) == 1 and sum([dif[num[r]] for r in result[0]]) == nodes):
            print("YES")
        else:
            print("NO")
    return

main()
