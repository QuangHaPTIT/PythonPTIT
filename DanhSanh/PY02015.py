


from math import *

if __name__ == '__main__':
    while True:
        ls = list(map(int, input().split()))
        lsecond = [0, 0, 0, 0]
        if ls == lsecond:
            break
        cnt = 0
        st = set(ls)
        while len(st) != 1:
           
            cnt += 1
            tmp = ls[0]
            for i in range(0, 3):
                ls[i] = abs(ls[i] - ls[i + 1])
            ls[3] = abs(ls[3] - tmp)
            st = set(ls)
        print(cnt)
