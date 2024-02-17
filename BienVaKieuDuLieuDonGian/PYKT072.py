











if __name__ == '__main__':
    ls = []
    cnt = 0
    ok = True
    for t in range(int(input())):
        s = input()
        ls.append(s)
    for i in range(1, len(ls), 1):
        res = ls[i]
        check = 0
        while(res != ls[0]):
            res = res[1:] + res[0:1]
            check += 1
            if check > len(ls[i]):
                ok = False
                break
            cnt += 1
    if not ok:
        print(-1)
    else:
        print(cnt)
