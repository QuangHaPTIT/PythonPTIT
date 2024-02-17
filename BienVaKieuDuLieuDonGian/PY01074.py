
from math import *
from array import array
max_int = 2 * int(1e6) + 1
prime = array('i', [0] * max_int)

def sang():
    global prime
    for i in range(1, max_int):
        prime[i] = i
    for i in range(2, isqrt(max_int) + 1):
        if prime[i] == i:
            for j in range(i * i, max_int, i):
                if prime[j] == j:
                    prime[j] = i

def sum_nt(n):
    global prime
    sum = 0
    while n != 1:
        sum += prime[n]
        n //= prime[n]
    return sum
if __name__ == '__main__':
    # for t in range(int(input())):
    sang()
    s = 0
    for t in range(int(input())):
        n = int(input())
        s += sum_nt(n)
    print(s)
