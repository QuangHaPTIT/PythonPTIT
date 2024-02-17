



from math import *

def Try(n , k):
    if k == pow(2, n - 1):
        return chr((n + 64) % 91)
    if k < pow(2, n - 1):
        return Try(n - 1, k)
    if k > pow(2, n - 1):
        return Try(n - 1, k - pow(2, n - 1))

if __name__ == '__main__':
    for t in range(int(input())):
        n, k = map(int, input().split())
        print(Try(n, k))