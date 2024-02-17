



def check(ls1:list, ls2:list):
    for i in range(len(ls1)):
        if ls1[i] > ls2[i]:
            return False
    return True




if __name__ == '__main__':
    for t in range(int(input())):
        n = int(input())
        ls1 = list(map(int, input().split()))
        ls2 = list(map(int, input().split()))
        ls1.sort()
        ls2.sort()
        
        if check(ls1, ls2):
            print("YES")
        else:
            print("NO")
