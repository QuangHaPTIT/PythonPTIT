




if __name__ == '__main__':
    n = int(input())
    a = []
    cnt = 0
    for i in range(n):
        a.append(input())
    for i in range(n):
        for j in range(n):
            if a[i][j] == 'C':
                for k in range(i + 1, n):
                    cnt += 1 if a[k][j] == 'C' else 0
                for k in range(j + 1, n, 1): cnt += 1 if a[i][k] == 'C' else 0

    print(cnt)