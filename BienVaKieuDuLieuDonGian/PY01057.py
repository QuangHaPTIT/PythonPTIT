

from math import *

def nt(a):
    for i in range(2, isqrt(a) + 1):
        if a % i == 0:
            return False
        
    return a >= 2

def check(s):
    for i in range(0, len(s), 1):
        if nt(int(s[i])) and not nt(i):
            return False
        elif not nt(int(s[i])) and nt(i):
            return False
    return True
            

if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")
        