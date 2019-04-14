#Santiago Melo Medina 2019-1

from sys import stdin
from collections import deque

def erathostenes(n):
    saved = [m for m in range(n+1)]
    primes = []
    for m in range(2,n+1):
        if saved[m]:
            s = m*m
            while s < n+1:
                saved[s] = 0
                s+=m
            primes.append(m)
    return primes

def factors(n):
    global primes, different
    prime = 0
    factor = primes[prime]
    result = 0
    while factor*factor <= n:
        power = 0
        if not n%factor: different.add(factor)
        while not n%factor:
            power+= 1
            n/=factor
        prime += 1
        result += power
        factor = primes[prime]
    if n!=1:
        result += 1
        different.add(int(n))
    return result

def decompose(n):
    global different, factores
    different = set()
    total = 0
    for s in range(2, n+1):
        value = factors(s)
        total += value
        factores[s] = [len(different), total]
    return

def main():
    global factores, primes
    primes = erathostenes(10**5)
    c = deque(''.join(stdin.readlines()).split())
    c.popleft()
    factores = {}
    decompose(10**5)
    while len(c):
        v = factores[int(c.popleft())]
        print("{} {}".format(v[0],v[1]))

main()
