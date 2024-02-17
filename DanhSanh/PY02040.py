




from math import *

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    k = int(input())
    sum_top = 0
    sum_bottom = 0
    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                sum_top += a[i][j]
            elif i + j > n - 1:
                sum_bottom += a[i][j]
    if abs(sum_top - sum_bottom) <= k:
        print("YES")
    else: print("NO")
    print(abs(sum_top - sum_bottom))