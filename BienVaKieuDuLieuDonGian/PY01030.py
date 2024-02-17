import math
def gcd(a, b):
    a = int(a); b = int(b)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def n_reverse(n):
    res = 0
    while n != 0:
        res += (n % 10)
        n //= 10
    return res

if __name__ == '__main__':
    cnt = 0
    n, k = map(str, input().split())
    for i in range(int(math.pow(10, int(k) - 1)), int(math.pow(10, int(k))), 1):
        if(gcd(n, str(i)) == 1):
            cnt += 1
            print(i, sep=" ", end=" ")
            if(cnt % 10 == 0):
                print()
        
    
