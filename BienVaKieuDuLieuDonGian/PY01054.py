







def muv_degit(a):
    res = 1
    while a != 0:
        x = a % 10
        if x != 0:
            res *= x
        a //= 10
    return res




if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        print(muv_degit(n))