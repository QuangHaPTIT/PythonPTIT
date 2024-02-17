def check(s):
    hit = 0
    for i in s:
        if i != '6' and i != '8':
            return False
        if i == '8':
            hit += 1
        else: hit = 0
        if hit == 3: return False
    return True


if __name__=='__main__':
    s = input()
    if check(s):
        print("YES")
    else:
        print("NO")