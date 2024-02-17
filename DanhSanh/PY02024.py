





from functools import cmp_to_key

def muv_degit(a):
    res = 1
    while a != 0:
        res *=  (a % 10)
        a //= 10
    return res


def cmp(a, b):
    x, y = muv_degit(a), muv_degit(b)
    if x != y:
        return x - y
    else: return a - b

if __name__ == '__main__':
    for t in range(int(input())):
        n,ls = int(input()), list(map(int, input().split()))
        ls.sort(key=cmp_to_key(cmp))
        for i in ls:
            print(i, end= " ")
        print()
