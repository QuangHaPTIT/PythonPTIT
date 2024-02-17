


def sum(n):
    while len(n) != 1:
        a = n[0:len(n) // 2]
        b = n[len(n) // 2:]
        print(int(a) + int(b))
        n = str(int(a) + int(b))

if __name__ == '__main__':
    n = input()
    sum(n)