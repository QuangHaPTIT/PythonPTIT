










if __name__ == '__main__':
    for t in range(int(input())):
        n, m = map(int, input().split())
        
        ls = [int(x) for x in input().split()]
        Max = max(ls)
        b = list()
        c = list()
        for i in range(len(ls)):
            if ls[i] == Max:
                ls.insert(i, m)
                break

        for i in ls:
            if i < 0:
                b.append(i)
            else:
                c.append(i)
        print(*b, sep=" ", end=" ")
        print(*c, sep=" ")