








if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        ls = list(map(int, input().split()))
        st = set(ls)
        M, m = 0, int(1e3 + 1)
        for i in ls:
            if i > M:
                M = i
            if i < m:
                m = i
        print(M - m + 1 - len(st))