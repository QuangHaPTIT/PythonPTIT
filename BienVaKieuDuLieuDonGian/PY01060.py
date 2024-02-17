





if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        res_index_even = 1
        sum_index_odd = 0
        ok = False
        for i in range(0, len(s)):
            if i % 2 == 0:
                if int(s[i]) != 0:
                    ok = True
                    res_index_even *= int(s[i])   
            else:
                sum_index_odd += int(s[i])
        if not ok:
            print(0, sum_index_odd, sep=" ")
        else:
            print(res_index_even, sum_index_odd, sep=" ")
