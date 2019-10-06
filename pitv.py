from collections import deque
from sys import stdin

def find(n):
    global parents
    if n == parents[n]:
        result = n
    else:
        result = find(parents[n])
        parents[n] = result
    return result

def kruskal(G, nodes):
    global parents
    G = sorted(G)
    parents = [n for n in range(nodes)]
    result = 0
    for w, u, v in G:
        if find(u) != find(v):
            parents[find(v)] = find(u)
            result += w
    return result

def main():
    cs = deque(''.join(stdin.readlines()).split())
    cs.popleft()
    case = 0
    while len(cs):
        if case: print()
        nodes, arcs = int(cs.popleft()), int(cs.popleft())
        keys, count = {}, 0
        G = []
        for _ in range(arcs):
            u, v, w = cs.popleft(), cs.popleft(), int(cs.popleft())
            if u not in keys:
                keys[u] = count
                count += 1
            if v not in keys:
                keys[v] = count
                count += 1
            u, v = keys[u], keys[v]
            G.append((w, u, v))
        print(kruskal(G, nodes))
        case += 1
    return

main()
