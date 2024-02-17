







# Đi theo từng cặp key và value, từng key trong đó sẽ là duy nhất, giống như map trong các ngôn ngữ khác

def dict3():
    # Đếm tần suất xuất hiện của phần tử trong mảng
    a = [1, 1, 2, 3, 4, 4, 3, 1, 6, 5, 4, 7]
    d = {}
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for val, fre in d.items():
        print(val, fre, sep=" ")

def dict1():
    a = ['name', 'dateofbirth', 'job']
    b = ['Pham Quang Ha', '22-02-2003', 'DEV']
    c = dict(zip(a, b))
    print(c)

def dict2():
    info = {
        'name' : 'Pham Quang Ha',
        'job' : 'dev',
        'salary' : '5000',
        'web' : 'quangha2003',
        'city' : 'HANOI'
    }
    # Thêm giá trị key, value cho dict khi chưa có key, hoặc khi có key rồi thì nó sẽ thay đổi value
    info['old'] = 10
    
    print(info['city'])
    print(info.keys())
    print(info.values())
    print(info.items())
    for key in info.keys():
        print(key, info[key], sep= " ")
if __name__ == '__main__':
    # a = [['name', 'Pham Quang Ha'],['dateofbirth', '22-02-2003'], ['job', 'DEV']]
    # b = dict(a)
    # print(b)
    # print(a)
    dict1()
    dict2()
    dict3()