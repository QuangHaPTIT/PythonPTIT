











if __name__ == '__main__':
    n, ls = int(input()), list(map(int, input().split()))
    for i in range(1, n + 2):
        if i not in ls:
            print(i)
            break
