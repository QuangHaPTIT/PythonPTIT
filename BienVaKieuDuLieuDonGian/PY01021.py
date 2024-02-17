








if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        sum = 0
        res = ''
        for i in s:
            if i.isalpha():
                res += i
            else: sum += int(i)
        tmp = sorted(res)
        print(''.join(tmp), sum, sep='')
