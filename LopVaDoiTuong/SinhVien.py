

class Person:

    def __init__(self, name, job):
        self.__name = name
        self.__job = job
    
    def infor(self):
        print('Name : {}, Job : {}'.format(self.__name, self.__job))





if __name__ == '__main__':
    p = Person('Pham Quang Ha', 'Dev')
    p.infor()