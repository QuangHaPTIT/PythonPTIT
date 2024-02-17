







    



if __name__ == '__main__':
    for t in range(int(input())):
        n ,m = map(int, input().split())
        ls = [[0 for _ in range(m)] for _ in range(n)]
        b = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            ls[i] = list(map(int, input().split()))
        for i in range(m):
            for j in range(n):
                b[i][j] = ls[j][i]
        c = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(m):
                    c[i][j] += ls[i][k] * b[k][j]
        for i in range(n):
            for j in range(n):
                print(c[i][j], end=" ")
            print("")