#Santiago Melo Medina 2019-1

from sys import stdin

def chimp(ladies, n):
    result = ""
    max, min = len(ladies)-1, 0
    if n > ladies[min]:
        while min < max-1:
            num = min + (max-min)//2
            if (ladies[num] >= n): max = num
            else: min = num
        if ladies[max] >= n: result += str(ladies[min]) + " "
        else: result += str(ladies[max]) + " "
    else: result += "X "
    max, min = len(ladies)-1, 0
    if n < ladies[max]:
        while min < max-1:
            num = min + (max-min)//2
            if (ladies[num] <= n): min = num
            else: max = num
        if ladies[min] <= n: result += str(ladies[max])
        else: result += str(ladies[min])
    else: result += "X"
    print(result)

def main():
    inp = stdin
    inp.readline()
    ladies = [ int(x) for x in inp.readline().split() ]
    inp.readline()
    queries = [ int(x) for x in inp.readline().split() ]
    for x in queries:
      chimp(ladies, x)

main()
