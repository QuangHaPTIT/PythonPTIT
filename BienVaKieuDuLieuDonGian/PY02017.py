



from collections import Counter





if __name__ == '__main__':
    for t in range(int(input())):
        n, ls = int(input()), list(map(int, input().split()))
        dc = list(dict(Counter(ls)).items())
        for i in range(len(dc)):
            if dc[i][1] % 2 == 1:
                print(dc[i][0])
                break
            