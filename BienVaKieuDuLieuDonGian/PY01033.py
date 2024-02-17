import math


if __name__ == '__main__':
    cnt = 0
    n, k = map(int, input().split())
   
    for i in range(n, k + 1, 1):
        for j in range(i + 1, k + 1, 1):
            if math.gcd(i, j) == 1:
                for l in range(j + 1, k + 1, 1):
                    if math.gcd(i, l) == 1 and math.gcd(j, l) == 1:
                        print(f'({i}, {j}, {l})')