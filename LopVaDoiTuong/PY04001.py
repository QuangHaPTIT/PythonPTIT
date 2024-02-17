





from decimal import Decimal
from math import *



class Point:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    def get_p1(self):
        return self.__p1
    def get_p2(self):
        return self.__p2
    def distance(self, x2):
        return ('%.4f' % (sqrt(pow(x2.get_p1() - self.__p1, 2) + (pow(x2.get_p2() - self.__p2, 2)))))

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1