import math

def snt(n):
    print("1 ", end="")
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu += 1
                n //= i
            res = "* " + str(i) + "^" + str(mu)
            print(res, sep=" ", end=" ")
    if n != 1:
        print("* " + str(n) + "^1", end="")


if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        snt(n)
        print()
        
        