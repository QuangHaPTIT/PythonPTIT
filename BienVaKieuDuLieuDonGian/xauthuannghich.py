

from math import *

def solve(s):
    for i in range(0, int(len(s) / 2)):
        if(s[i] != s[len(s) - i - 1]):
            return False
        
    return True

if __name__ == '__main__':

    ls = list(map(str, input().split()))
    ls1 = []
    for i in ls:
        if solve(i):
            ls1.append(i)
    ls1.sort()
    for i in ls1:
        print(i, end=" ")