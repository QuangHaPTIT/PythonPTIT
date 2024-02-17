






from math import *


if __name__ == '__main__':
    n, ls = int(input()), list(map(int, input().split()))
    ls.sort()
    for i in range(0, len(ls)):
        for j in range(i + 1, len(ls)):
            if gcd(ls[i], ls[j]) == 1:
                print(ls[i],ls[j], sep=" ")