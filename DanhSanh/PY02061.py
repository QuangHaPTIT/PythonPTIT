







import numpy as np



if __name__ == '__main__':
    for t in range(int(input())):
        n, m = map(int, input().split())
        a = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            a[i] = list(map(int, input().split()))
        b = [[0 for _ in range(3)] for _ in range(3)]
        for i in range(3):
            b[i] = list(map(int, input().split()))
        convolution = np.co
