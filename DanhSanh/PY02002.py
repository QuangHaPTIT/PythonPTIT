








if __name__ == '__main__':
    a = [0] * 93
    a[0] = 1
    a[1] = 1
    for i in range(2, 93):
        a[i] = a[i - 1] + a[i - 2]
    
    for t in range(int(input())):
        x, y = map(int, input().split())
        for i in range(x - 1, y):
            print(a[i], end=" ")
        print()