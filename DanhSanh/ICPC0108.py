





if __name__ == '__main__':
    for t in range(int(input())):
        n, ls = int(input()), list(map(int, input().split()))
        ls.sort()
        cnt = 0
        for i in range(n - 2):
            lf, right = i + 1, n - 1
            while lf < right:
                temp = ls[i] + ls[lf] + ls[right]
                if not temp:
                    cnt += 1
                    lf += 1
                elif temp < 0:
                    lf += 1
                else:
                    right -= 1
        print(cnt)
