



from math import *



if __name__ == '__main__':
    for t in range(int(input())):
        n, ls = int(input()), list(map(int,input().split()))
        a = [0] * 1000001
        mx = 0
        x:int
        for i in ls:
            a[i] += 1
            if mx < a[i]:
                mx = a[i]
                x = i
        if(mx > n // 2):
            print(x)
        else: print("NO")
            
