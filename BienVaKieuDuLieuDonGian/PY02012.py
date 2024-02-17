






if __name__ == '__main__':
    n = int(input())
    ls = list(map(int, input().split()))
    a, b = [], []
    for i in ls:
        if i % 2 == 0:
            a.append(i)
        else:
            b.append(i)
    a.sort()
    l = 0
    b.sort(reverse=True)
    j = 0
    
    for i in ls:
        if i % 2== 0 and l < len(a):
            print(a[l], end=" ")
            l += 1
        if i % 2 == 1 and j < len(b):
            print(b[j], end=" ")
            j+= 1