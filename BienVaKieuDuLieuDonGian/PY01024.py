
import math
def check(n):
    l = len(n)
    s = 0
    for i in range(1, l, 1):
        if abs(int(n[i]) - int(n[i - 1])) != 2:
            return "NO"
        s += int(n[i])
    s += int(n[0])
    if s % 10 != 0:
        return "NO"
    return "YES"

if __name__ == '__main__':
    for t in range(int(input())):
        n = input()
        print(check(n))