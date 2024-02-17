import math

def check(a):
    for i in range(2, int(math.sqrt(a) + 1), 1):
        if( a % i == 0):
            return False
    return a >= 2

def check_nt(a):
    if(check(len(a)) == False):
        return 'NO'
    count = 0
    for i in a:
        if(check(int(i))):
            count += 1
    if(count <= len(a) - count):
        return 'NO'
    return 'YES'


if __name__ == '__main__':
    for t in range(int(input())):
        print(check_nt(input()))