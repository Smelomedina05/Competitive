from collections import deque
from sys import stdin

def game(piedras, match):
    result = piedras
    for s in range(len(match)):
        condition1 = s+1 < len(match) and match[s+1] == "o" and s+2 < len(match) and match[s+2] == "-"
        condition2 = s-1 < len(match) and match[s-1] == "o" and s-2 < len(match) and match[s-2] == "-"
        if match[s] == "o":
            if condition1:
                match[s] = "-"; match[s+1] = "-"; match[s+2] = "o"
                result = min(result, game(piedras-1, match))
                match[s] = "o"; match[s+1] = "o"; match[s+2] = "-"
            elif condition2:
                match[s] = "-"; match[s-1] = "-"; match[s-2] = "o"
                result = min(result, game(piedras-1, match))
                match[s] = "o"; match[s-1] = "o"; match[s-2] = "-"
    return result

def main():
    c = deque(''.join(stdin.readlines()).split())
    c.popleft()
    while len(c):
        tmp = c.popleft()
        piedras = 0
        match = []
        for n in tmp:
            match.append(n)
            if n == "o":
                piedras += 1
        print(game(piedras, match))

main()
