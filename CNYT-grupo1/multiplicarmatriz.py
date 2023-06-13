from sys import stdin
def crear(n,m):
    ma = []
    for i in range(n):
        l = []
        for j in range(m):
            l.append(0)
        ma.append(l)
    return ma
def multiplicar(m1,m2):
##    print(m1,m2)
    if len(m1[0]) == len(m2): 
        m = crear(len(m1),len(m2[0]))
        for i in range(len(m)):
            for j in range(len(m[0])):
                for k in range(len(m2)):
                    #print(m[i][j])
                    m[i][j] += m1[i][k]*m2[k][j]
        return m
    else:
        return [0,0,0]

def mostrar(m):
    for i in m:
        print(*i)
def main():
    print("n de filas 1 matriz")
    n = int(stdin.readline())
    matriz1 = []
    for i in range(n):
        lista = [int(x) for x in stdin. readline().strip().split()]
        matriz1.append(lista)
    print("m de filas matriz 2")
    m = int(stdin.readline())
    matriz2 = []
    for j in range(m):
        lista2 = [int(y) for y in stdin.readline().strip().split()]
        matriz2.append(lista2)
    k = 0
##    mostrar(matriz1)
##    print()
##    mostrar(matriz2)
    while matriz2[0][0] <= 1000:
        
##        mostrar(matriz1)
##        print("---")
##        mostrar(matriz2)
        matriz2 = multiplicar(matriz2,matriz1)
        k += 1
    print(k)
main()
