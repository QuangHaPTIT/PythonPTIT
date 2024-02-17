








from math import *



if __name__ == '__main__':
    s = (input())
    ans = 0
    while len(s) != 1:
        ans += 1
        sum = 0
        for i in s:
            sum += (ord(i) - ord('0'))
        s = str(sum)
    print(ans)
            