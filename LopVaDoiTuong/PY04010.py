





class ThiSinh:
    def __init__(self, name, dateOfBirth, sub1:float, sub2:float, sub3:float):
        self.__name = name
        self.__dateOfBirth = dateOfBirth
        self.__sub1 = sub1
        self.__sub2 = sub2
        self.__sub3 = sub3

    def tongDiem(self):
        return '%.1f' % (self.__sub1 + self.__sub2 + self.__sub3)
    
    def __str__(self):
        return self.__name + " " + self.__dateOfBirth + " " + self.tongDiem()





if __name__ == '__main__':
    p = ThiSinh(input(), input(), float(input()), float(input()), float(input()))
    print(p)