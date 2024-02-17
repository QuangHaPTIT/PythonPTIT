

def solve(n):
    for i in range(1000):
        if n % 7 == 0:
            return n
        rn = int(str(n)[::-1])
        n += rn
    return -1




if __name__ == '__main__':
    for t in range(int(input())):
        print(solve(int(input())))