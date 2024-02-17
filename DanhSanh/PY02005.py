










if __name__ == '__main__':
    n, list, cnt = int(input()), [int(x) for x in input().split()], 0
    for i in range(0, n, 1):
        for j in range(i + 1, n, 1):
            if list[i] > list[j]:
                cnt += 1
    print(cnt)