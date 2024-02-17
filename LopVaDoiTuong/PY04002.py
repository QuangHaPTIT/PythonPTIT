







class Rectangle:
    def __init__(self, x0, x1, x2):
        self.__x0 = x0
        self.__x1 = x1
        self.__x2 = x2
    def perimeter(self):
        return (self.__x0 + self.__x1) * 2
    
    def area(self):
        return self.__x0 * self.__x1
    def color(self):
        return self.__x2.title()




if __name__ == '__main__':
    arr = input().split()
    if int(arr[0]) > 0 and int(arr[1]) > 0:
        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print("{} {} {}".format(r.perimeter(), r.area(), r.color())) 
    else: print("INVALID")  