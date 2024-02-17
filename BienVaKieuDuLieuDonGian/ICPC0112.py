

from math import *

max_int = int(1e6 + 1)
prime = [1] * max_int

def sang():
    global prime
    prime[0] = prime[1] = 0
    for i in range(2, isqrt(max_int) + 1, 1):
        if prime[i]:
            for j in range(i * i, max_int, i):
                prime[j] = 0


if __name__ == '__main__':
    sang()
    for t in range(int(input())):
        n = int(input())
        cnt = 0
        for i in range(n, 6, -1):
            if (prime[i] and prime[i - 2] and prime[i - 6]) or (prime[i] and prime[i - 4] and prime[i - 6]):
                cnt += 1
        print(cnt)