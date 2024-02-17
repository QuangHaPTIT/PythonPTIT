def check_cs(a):
    for i in a:
        if(i != '1' and i != '0' and i != '2'):
            return 'NO'
        
    return 'YES'


if __name__ == '__main__':
    for t in range(int(input())):
        print(check_cs(input()))