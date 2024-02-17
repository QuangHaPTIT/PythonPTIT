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

for t in range(int(input())):
    n = input()
    if(gcd(n, n[::-1]) == 1):
        print("YES")
    else:
        print("NO")
    
