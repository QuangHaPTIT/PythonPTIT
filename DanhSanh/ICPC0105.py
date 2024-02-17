

import re


def regEX(s):
    res = re.findall(r'\d+', s)
    ls = [int(x) for x in res if len(x) >= 1]
    print(max(ls))


if __name__ == '__main__':
    for t in range(int(input())):
        regEX(input())