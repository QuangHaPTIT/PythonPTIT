






def number_b(a):
    a1 = int(a[0])
    a2 = int(a[1])
    s = ''
    for i in range(0, len(a), 1):
        if i % 2 == 0: s += str(a1)
        else: s += str(a2)
    if a == s : return 'YES'
    else : return 'NO'



if __name__ == '__main__':
    for t in range(int(input())):
        print(number_b(input()))