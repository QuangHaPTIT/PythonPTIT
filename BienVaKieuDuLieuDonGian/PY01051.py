
def thuanNghich(a:str):
    if(len(a) <= 1):
        return False
    b = a[::-1]
    if b == a:
        return True
    else: return False

def sum(a):
    s = 0
    for i in a:
        s += int(i)
    return s
if __name__ == '__main__':
    for t in range(int(input())):
        if thuanNghich(str(sum(input()))):
            print("YES")
        else: print("NO")
