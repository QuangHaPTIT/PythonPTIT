








if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        ls = list(map(int, input().split()))
        m1 = -int(1e8) - 1
        m2 = -int(1e8) - 2
        m3 = -int(1e8) - 3
        for i in ls:
            if i > m1:
                m1 = i
            if i > m2 and i != m1:
                m2 = i
            if i > m3 and i != m1 and i != m2:
                m3 = i
        print(m1 + m2 + m3)