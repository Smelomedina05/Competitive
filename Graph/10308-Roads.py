from sys import stdin
from collections import deque

def main():
    c = deque(''.join(stdin.readlines()).split("\n"))
    m, p, graph, counter = {}, {}, [], 0
    while len(c):
        s = c.popleft()
        if s != '':
            s = s.split()
            for r in s:
                if r not in m:
                    m[r] = counter
                    counter += 1
                    graph.append([])
            p[(m[s[0]], m[s[1]])] = int(s[2])
            graph[m[s[0]]].append(m[s[1]])
            graph[m[s[1]]].append(m[s[0]])
        else:
            m, p, graph, counter = {}, {}, [], 0




main()
