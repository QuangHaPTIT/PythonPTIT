











if __name__ == '__main__':
    ok , k, a = 0, [], []
    for t in range(int(input())):
        s = input().split()
        if len(a) == 0 and len(s) == 6: k.append(1)
        a.append(s)
        if len(a) > 1 and len(s) == 6 and len(a[-2]) == 7: k.append(1)
        if len(s) == 7:
            ok += 1
        if ok == 4:
            k.append(2)
            ok = 0
    print(len(k))
    print(*k, sep="\n")
