











if __name__ == '__main__':
    for t in range(int(input())):
        s, n = input(), input()
        c = 0
        temp_pos = 0
        check = s.find(n, 0)
        while check != -1:
            c += 1
            
            
            check = s.find(n, check + len(n))
        print(c)