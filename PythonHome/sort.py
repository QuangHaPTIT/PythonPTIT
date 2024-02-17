
from functools import cmp_to_key

def sum_degit(a):
    sum = 0
    while a != 0:
        sum += (a%10)
        a //= 10
    return sum

def sort1():
    a = [-1, -4, - 9, 10, 11, -3]
    a.sort(key= abs, reverse= True)
    print(a)

def sort2():
    a = [[1, 2], [3, 2], [1, 1], [4, 1], [3, 6]] # Nested list
    a.sort(key= lambda x : x[0]) # x[0] là phần tử đầu tiên trong từng nested
    a.sort(key= lambda x : (x[0], x[1])) # Xắp xếp theo thằng thứ nhất tăng dần, nếu 2 thằng bằng nhau thì xắp xếp theo thằng thứ 2 tăng dần

def cmp(a, b):
    return a - b
def sort3():
    # Dùng functools
    a = [10, 2, 3, 15, 20, 98, 10]
    a.sort(key= cmp_to_key(cmp))
    print(a)
if __name__ == '__main__':
    for t in range(int(input())):
        n, ls = int(input()), list(map(int, input().split()))
        ls.sort(key=sum_degit)
        print(ls)
        sort3()