import math

def nt(a):
    if(a < 2): return 'NO'
    for i in range(2, int(math.sqrt(a) + 1), 1):
        if(a % i == 0):
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    for t in range(int(input())):
        b = input()
        a = int(b[len(b) - 4:len(b)])
        print(nt(a))