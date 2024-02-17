








if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        ls = list(map(int, input().split()))
        res = []
        temp = [0] * n
        for i in range(n):
            while len(res) > 0 and ls[res[-1]] <= ls[i]:
                res.pop()
            temp[i] = i + 1 if len(res) == 0 else i - res[-1]
            res.append(i)
        print(*temp)