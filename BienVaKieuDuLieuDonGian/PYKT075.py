










if __name__ == '__main__':
    f = open("SOTAY.txt", "r")
    # f1 = open("DIENTHOAI.txt", "w")
    ls = list([])
    tmp = ''
    res = ''
    ok = 0
    for line in f:
        if line == "\n": continue
        if line[:4] == "Ngay":
            tmp = line
        else:
            if ok == 0:
                res += (line + ": ")
                ok += 1
            else:
                res += line
                ok = 0
                ls.append([res, tmp])
    for i in ls:
        print(i[0], i[1], sep=" ")