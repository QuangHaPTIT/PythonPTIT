


from math import *

class PhanSo:
    def __init__(self, x1:int, x2:int):
        self.__x1 = x1
        self.__x2 = x2

    def get_x1(self):
        return self.__x1
    def get_x2(self):
        return self.__x2

    def caculator(self, p2):
        temp1 = self.__x1 * p2.get_x2() + self.__x2 * p2.get_x1()
        temp2 = self.__x2 * p2.get_x2()
        gcd_t1t2 = int(gcd(temp1, temp2))
        temp1 = temp1 / gcd_t1t2
        temp2 = temp2 / gcd_t1t2
        return '{}/{}'.format(int(temp1), int(temp2))
    def __str__(self):
        return self.caculator()



if __name__ == '__main__':
    a1, a2, b1, b2 = map(int, input().split()) 
    p = PhanSo(a1, a2)
    p2 = PhanSo(b1, b2)
    print(p.caculator(p2))