#Santiago Melo Medina 20191

from sys import stdin

global count

def adyacent(n, m, cadenas):
    new = []
    valores = [(-1,1), (-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1)]
    for v in valores:
        if n+v[0] >= 0 and n+v[0] < len(cadenas) and m+v[1] >= 0 and m+v[1] < len(cadenas[n]):
            new.append((n+v[0],m+v[1]))
    return new

def dfs(n, m, cadenas):
    global count
    var = cadenas[n][m]
    list = adyacent(n, m, cadenas)
    if not cadenas[n][m].isdigit():
        cadenas[n][m] = str(count)
        for v in list:
            if cadenas[v[0]][v[1]] == var:
                dfs(v[0], v[1], cadenas)
    else:
        count -= 1


def forest(cadenas):
    global count
    mat = ""
    for n in range(len(cadenas)):
        for m in range(len(cadenas[n])):
            dfs(n, m, cadenas)
            count += 1
    maxrow = len(cadenas)
    maxcol = len(cadenas[0])
    r, c = 0, 0
    sizes = []
    while (c < maxcol):
        r = 0
        sizes.append(0)
        while (r < maxrow):
            if len(str(cadenas[r][c])) > sizes[c]: sizes[c] = len(str(cadenas[r][c]))
            r += 1
        c += 1
    for n in range(len(cadenas)):
        for m in range(len(cadenas[n])):
            mat += " "*(sizes[m]-len(str(cadenas[n][m]))) + cadenas[n][m] + " "
        mat = mat[:-1] + "\n"
    print(mat+"%")

def main():
    global count
    tmp = stdin
    cadenas = []
    cadena = tmp.readline()
    while(cadena):
        while(cadena[:-1] != "%" and cadena):
            cadenas.append(cadena[:-1].split(" "))
            cadena = tmp.readline()
        count = 1
        forest(cadenas)
        cadenas = []
        cadena = tmp.readline()


main()
