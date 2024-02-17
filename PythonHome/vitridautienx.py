
# Tìm vị trí xuất hiện đầu tiên của phần tử có giá trị X trong mảng đã sắp
# xếp tăng dần

def first_pos(a:list, l,  r, x):
    res = -1
    while l <= r:
        m = (l + r) //2
        if a[m] == x:
            res = m
            r = m - 1
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return res   

# Tìm vị trí xuất hiện đầu tiên của phần tử có giá trị lớn hơn X trong mảng đã sắp
# xếp tăng dần
def first_pos_larger_x(a:list, l, r, x):
    res = -1
    while l <= r:
        m = (l + r) // 2
        if a[m] > x:
            res = m
            r = m - 1
        else:
            l = m + 1
    return res

if __name__ == '__main__':
    n,ls, x= int(input()), list(map(int, input().split())), int(input())
    print(first_pos(ls, 0, len(ls) - 1, x))
    print(first_pos_larger_x(ls, 0, len(ls) - 1, x))

