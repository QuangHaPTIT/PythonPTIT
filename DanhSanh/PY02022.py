



from math import *

def nt(a):
    for i in range(2, isqrt(a) + 1):
        if a % i == 0:
            return False
    return a >= 2





if __name__ == '__main__':
    n, ls = int(input()), list(map(int, input().split()))
    a = [0] * 1000000
    for i in ls:
        a[i] += 1
    for i in ls:
        if nt(i) and a[i] != 0:
            print(i, a[i], sep=" ")
            a[i] = 0
    