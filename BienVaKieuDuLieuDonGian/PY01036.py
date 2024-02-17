



if __name__ == '__main__':
    for t in range(0, int(input())):
        s = 0
        for i in range(int(input()), 0, -2):
            s += 1 / i

        print(f'{s:.6f}')