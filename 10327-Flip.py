#Santiago Melo Medina 2019-1

from sys import stdin

def mS(a, first, last):
    result = 0
    if first < last:
        middle = first + ((last - first)>>1)
        result += mS(a, first, middle)
        result += mS(a, middle+1, last)
        result += sum(a, first, middle, last)
    return result

def sum(a, first, middle, last):
    result = 0
    limitl, limitr = middle-first+1, last-middle
    L = [a[first + n] for n in range(0, middle-first+1)]
    R = [a[middle + n] for n in range(1, last-middle+1)]
    n, m, count = 0, 0, first
    while n < limitl and m < limitr:
        if (L[n] <= R[m]):
            a[count] = L[n]
            n += 1
        else:
            a[count] = R[m]
            result += len(L) - n
            m += 1
        count += 1
    while n < limitl:
        a[count] = L[n]
        n += 1
        count += 1
    while m < limitr-1:
        a[count] = R[m]
        m += 1
        count += 1
    return result

def main():
  inp = stdin
  s = inp.readline()
  lab = "Minimum exchange operations : {0}"
  while len(s)>0:
    n = int(s)
    num = [int(x) for x in inp.readline().strip().split()]
    print(lab.format(mS(num, 0, n-1)))
    s = inp.readline().strip()

main()
