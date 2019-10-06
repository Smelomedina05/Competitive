from collections import deque
from sys import stdin

def intervalCovering(A, l):
    A = sorted(A)
    ancker, i = 0, 0
    count, hole = 0, 0
    while i < len(A) and ancker < l and not hole:
        hole = A[i][0] > ancker
        longest = i
        i += 1
        while  i < len(A) and A[i][0] <= ancker:
            if A[i][1] > A[longest][1]:
                longest = i
            i += 1
        ancker = A[longest][1]
        count += 1
    return count if not hole and ancker >= l else -1

def main():
    cs = deque(''.join(stdin.readlines()).split())
    while len(cs)-2:
        l, g = int(cs.popleft()), int(cs.popleft())
        G = []
        for _ in range(g):
            x, r = int(cs.popleft()), int(cs.popleft())
            G.append((x-r, x+r))
        result = intervalCovering(G, l)
        if result != -1:
            print(len(G)-result)
        else:
            print(result)
    return

main()
