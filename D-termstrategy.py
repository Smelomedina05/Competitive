from collections import deque
from sys import stdin

### n : course
### s : hour
### res : hours left
### R : subject to study
### Y : hours spent on subject R
### G[y] : grade on subject R for y hours

### max mark :
###     -infinite              ; study more hours than available
###     term(n,s+1, res) ; G(Y) < 5
###     max(term(n+1,s=0, res-(Y), acum+G(Y)), term(n,s+1, res)) ; G(Y) >= 5

def term(L, n, s, res):
    global memo
    key = (n,res)
    if key in memo:
        result = memo[key]
    else:
        if n == len(L) and res >= 0:
            result = 0
        elif res < 0:
            result = float("-inf")
        else:
            result = float("-inf")
            for s in range(len(L[0])):
                if L[n][s] >= 5:
                    result = max(result, term(L, n+1, s, res-(s+1))+L[n][s])
        memo[key] = result
    return result

def main():
    global memo
    cs = deque(''.join(stdin.readlines()).split())
    cs.popleft()
    while len(cs):
        n, m = int(cs.popleft()), int(cs.popleft())
        memo = {}
        L = [[int(cs.popleft()) for _ in range(m)] for _ in range(n)]
        result = term(L, 0, 0, m)/len(L)
        print("Maximal possible average mark - {:.2f}.".format(result) if result != float("-inf") else "Peter, you shouldn't have played billiard that much.")
    return

main()
