def check(a):
    if(len(a) % 2 != 0): return False
    b = a[::-1]
    if(b != a) : return False
    for i in a:
        if(int(i) % 2 != 0):
            return False
    
    return True

if __name__ == '__main__':
    for t in range(int(input())):
        for i in range(22, int(input()), 2):
            if check(str(i)):
                print(i,  end=' ')
        print()