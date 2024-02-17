



from math import *

def nt(a):
    for i in range(2, isqrt(a) + 1):
        if(a % i == 0):
            return False
    return a >= 2




if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(m):
            print("1", end=" ") if nt(a[i][j]) == True else print("0", end=" ")
        print()
            