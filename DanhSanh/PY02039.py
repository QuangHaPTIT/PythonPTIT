







from math import *


if __name__ == '__main__':
    n = int(input())
    a = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        a[i] = list(map(int, input().split()))
    k = int(input())
    sum_top = 0
    sum_bottom = 0
    for i in range(n):
        for j in range(n):
            if i > j:
                sum_top += a[i][j]
            elif j > i:
                sum_bottom += a[i][j]
    if abs(sum_top - sum_bottom) <= k:
        print("YES")
    else:
        print("NO")
    print(abs(sum_top - sum_bottom))

