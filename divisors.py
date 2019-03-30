# Santiago Melo Medina 2019-1

import math
from sys import stdin
from collections import deque

def erathostenes(n):
    saved = [m for m in range(n+1)]
    primes = []
    for m in range(2, n+1):
        if saved[m]:
            s = m * m
            while s < n+1:
                saved[s] = 0
                s += m
            primes.append(m)
    return primes

def divisors(n):
    global primes
    prime = 0
    factor = primes[prime]
    result = 1
    while factor*factor <= n:
        power = 0
        while not n%factor:
            n /= factor
            power += 1
        result *= (power+1)
        prime += 1
        factor = primes[prime]
    if n != 1: result *= 2
    return result

def higher(f, s):
    high = (f, 0)
    while f <= s:
        value = divisors(f)
        if high[1] < value:
            high = (f, value)
        f += 1
    return high

def main():
    global primes
    primes = erathostenes(10**5)
    c = deque(''.join(stdin.readlines()).split())
    c.popleft()
    while len(c):
        values = int(c.popleft()), int(c.popleft())
        nums = higher(values[0], values[1])
        print("Beetween {} and {}, {} has a maximum of {} divisors.".format(values[0], values[1], nums[0], nums[1]))

main()
