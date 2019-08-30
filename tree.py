from collections import deque
from sys import stdin

def assign(ino, pos):
    global order, poso
    poso = pos
    result = []
    for n in range(len(pos)): order[pos[n]] = n
    for n in ino: result.append(order[n])
    return result

def preinpos(A):
    global order, poso
    tree = []
    if len(A):
        index = A.index(max(A))
        L = A[:index]
        R = A[index+1:]
        tree = [int(poso[A[index]]), preinpos(L), preinpos(R)]
    return tree

def sum(t, acum):
    global sums, lvs
    if len(t[1]): sum(t[1], acum+t[1][0])
    if len(t[2]): sum(t[2], acum+t[2][0])
    if not len(t[1]) and not len(t[2]):
        sums.append(acum)
        lvs.append(t[0])




def main():
    global order, poso, sums, lvs
    c = deque(stdin.readlines())
    while len(c):
        order, poso, r = {}, [], []
        sums, lvs = [], []
        inorder = deque(c.popleft().split())
        posorder = deque(c.popleft().split())
        t = preinpos(assign(inorder, posorder))
        sum(t, t[0])
        indices, minimo = [], float("inf")
        for s in range(len(sums)):
            if sums[s] < minimo:
                minimo = sums[s]
        for s in range(len(sums)):
            if minimo == sums[s]: indices.append(lvs[s])
        print(min(indices))


main()
