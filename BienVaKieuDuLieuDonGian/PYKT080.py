



path = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

d = [[0] * 101 for _ in range(101)]
s = 0
ls = list([])
def Try(i, j, n, m):
    for x in path:
        global s
        i1, j1 = i + x[0], j + x[1]
        if i1 >= 0 and i1 < n and j1 >= 0 and j1 < m and d[i1][j1] == 0:
            d[i1][j1] = 1
            s += ls[i1][j1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        ls.append([int(x) for x in input().split()])
    for i in range(n):
        for j in range(m):
            if ls[i][j] == -1:
                Try(i, j, n, m)
    print(s)