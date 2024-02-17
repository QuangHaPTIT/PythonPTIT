

from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input()) # cửa sổ trượt k
    tong = sum(a[:k])
    print(tong,end=' ')
    for i in range(1, n - k + 1, 1):
        tong = tong - a[i - 1] + a[k + i - 1]
        print(tong, end=' ') 