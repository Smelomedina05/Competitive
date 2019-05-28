#Santiago Melo Medina 20191

from sys import stdin
from collections import deque


def topo(n, new, ids, visited, final):
    visited[n] = 1
    for m in new[n]:
        if visited[ids.index(m)] == 0:
            topo(ids.index(m), new, ids, visited, final)
    if ids[n] not in final: final.appendleft(ids[n])

def arctoList(new):
    list, ids = [], []
    dict = {}
    counter = 0
    for n in new:
        if not n[0] in dict:
            dict[n[0]] = counter
            list.append([])
            ids.append(n[0])
            list[dict[n[0]]].append(n[1])
            counter += 1
        else:
            list[dict[n[0]]].append(n[1])
    return (list, ids)


def rare(list):
    new = []
    words = []
    for n in range(len(list)-1):
        for m in list[n]:
            if m not in words: words.append(m)
        centinel = True
        b = 0
        while b < len(list[n]) and b < len(list[n+1]) and centinel:
            if list[n][b] != list[n+1][b]:
                new.append((list[n][b], list[n+1][b]))
                centinel = False
            b +=1
    for m in list[len(list)-1]:
        if m not in words: words.append(m)
    new = arctoList(new)
    for n in words:
        if n not in new[1]:
            new[1].append(n)
            new[0].append([])
    visited = [0 for n in new[1]]
    final = deque()
    for n in range(len(new[1])):
        topo(n, new[0], new[1], visited, final)
    print(''.join(final))


def main():
    list = []
    for cadena in stdin:
        if str(cadena)[:-1] == "#":
            rare(list)
            list = []
        else:
            list.append(str(cadena)[:-1])

main()
