




from math import *


def nt(a):
    for i in range(2, isqrt(a) + 1):
        if(a % i == 0):
            return False
    return a >= 2



def sum(a:str):
    s = 0
    for i in a:
        s += int(i)
    return s

if __name__ == '__main__':
    for t in range(int(input())):
        if nt(sum(input())) :
            print("YES")
        else: print("NO")