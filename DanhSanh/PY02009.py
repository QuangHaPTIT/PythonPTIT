











from math import *


if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        list = [0] * 1001
        max1 = 0
        for i in range(n):
            x = int(input())
            list[x] += 1
            max1 = max(list[x], max1)
        for i in range(0, 1001):
            if(list[i] == max1):
                print(i)
                break

        
            