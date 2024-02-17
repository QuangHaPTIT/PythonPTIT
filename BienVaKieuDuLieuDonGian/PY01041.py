
def solve(a):
    if(len(a) < 3):
        return 'NO'
    ar = list(int(i) for i in a)
    up = True
    for i in range(1, len(a), 1):
        if up and ar[i] <= ar[i - 1]:
            up = False
        elif not up and a[i] >= a[i - 1]:
            return 'NO'
    return 'YES'


if __name__ == '__main__':
    for t in range(int(input())):
        print(solve(input()))