

from math import *
N = 10**18
list = []

i = 1
while i <= N:
    j = 1
    while j <= N:
        k = 1
        while k <= N:
            list += [i * j * k]
            k *= 5
        j *= 3
    i *= 2
list.sort()

def binseach(l, r, x):
    while(l <= r):
        m = (l + r) // 2
        if(list[m] == x):
            return m + 1
        if list[m] > x:
            r = m - 1
        else:
            l = m + 1
    return 'Not in sequence'

    


if __name__ == '__main__':
    for t in range(int(input())):
        print(binseach(0, len(list), int(input())))