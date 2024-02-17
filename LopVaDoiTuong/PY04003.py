


from math import *


class PhanSo:
    def __init__(self, x1, x2):
        self.__x1 = x1
        self.__x2 = x2
    
    def caculator(self):
        a = int(self.__x1 / gcd(self.__x1, self.__x2))
        b = int(self.__x2 / gcd(self.__x1, self.__x2))
        return '{}/{}'.format(a, b)
    def __str__(self):
        return self.caculator()




if __name__ == '__main__':
    a, b = map(int, map(int, input().split()))
    p = PhanSo(a, b)
    print(p)
