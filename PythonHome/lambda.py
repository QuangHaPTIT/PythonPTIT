








if __name__ == '__main__':
    #res = (lambda x : x ** 2)(10)
    #print(res)
    #res1 = lambda x : x ** 3
    #print(res1(10))
    func = lambda x, y, z : x + y + z
    print(func(100, 200, 300))
    a = [1, 2, 3, 4, 5]
    b = list(map(lambda x : x * 2, a))
    print(b)
    findMax = lambda x, y : x if x > y else y
    print(findMax(100, 200))





