











if __name__ == '__main__':
    
    for t in range(int(input())):
        n, list1, list2 = int(input()), [int(x) for x in input().split()], [int(x) for x in input().split()]
        list1.sort()
        list2.sort()
        ok = True
        for i in range(n):
            if(list1[i] > list2[i]):
                ok = False
                break
        if ok:
            print("YES")
        else:
            print("NO")

