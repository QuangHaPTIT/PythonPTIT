





from math import *


if __name__ == '__main__':
    n, ls = int(input()), list(map(float, input().split()))
    mx = max(ls)
    mn = min(ls)
    newlist = [x for x in ls if x != mx and x !=  mn]
    print(f'{sum(newlist)/len(newlist):.2f}')
    