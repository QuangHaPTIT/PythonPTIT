
from math import *
from functools import cmp_to_key


def sum_degit(a):
    sum  = 0
    while a != 0:
        sum += (a % 10)
        a //= 10
    return sum

def cmp(a, b):
    if sum_degit(a) != sum_degit(b):
        return sum_degit(a) - sum_degit(b)
    else:
        return a - b




if __name__ == '__main__':
    for t in range(int(input())):
        n, ls = int(input()),list(map(int, input().split()))
        ls.sort(key=cmp_to_key(cmp))
        for i in ls:
            print(i, end= " ")
        print()