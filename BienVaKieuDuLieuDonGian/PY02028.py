


from math import *
from functools import cmp_to_key

def checknt(a):
    for i in range(2, isqrt(a) + 1, 1):
        if a % i == 0:
            return False
    return a > 1

    

if __name__ == '__main__':
    n = int(input())
    ls = list(map(int, input().split()))
    a = [x for x in ls if checknt(x)]
    a.sort()
    j = 0
    for i in ls:
        if checknt(i):
            print(a[j], end=" ")
            j += 1
        else:
            print(i, end=" ")