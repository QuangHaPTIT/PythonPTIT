







def sum_muv_degit(a:str):
    sum = 0
    res = 1
    ok = False
    for i in range(len(s)):
        if i % 2 == 0:
            sum += int(a[i])
        else:
            if not ok and int(a[i]) != 0:
                ok = True
            if int(s[i]) != 0:
                res *= int(a[i])
    print(sum, end= " ")
    if ok:
        print(res)
    else: print(0)


if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        sum_muv_degit(s)
