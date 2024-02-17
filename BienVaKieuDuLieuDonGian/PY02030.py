





from collections import Counter
from math import *
def checknt(a):
    for i in range(2, isqrt(a) + 1):
        if a % i == 0:
            return False
    return a >= 2

if __name__ == '__main__':
    
    n = int(input())
    
    ls = list(map(int, input().split()))
    dc = list(dict(Counter(ls)).items())
    ls = []
    for i in range(len(dc)):
        ls.append(dc[i][0])
    pre = [0] * (len(ls) + 1)
    pre[0] = ls[0]
    for i in range(1, len(ls)):
        pre[i] = pre[i - 1] + ls[i]
    ok = False
    for i in range(len(ls)):
        if checknt(pre[i]) and checknt(pre[len(ls) - 1] - pre[i]):
            print(i)
            ok = True
            break
    if not ok:
        print("NOT FOUND")