

def check(a):
    for i in a:
        if (ord(i) < 97 or ord(i) > 122) and i != '.' and i != '_':
            return False
    return True


if __name__ == '__main__':
    s = input()
    s = s.lower()
    b = s[:len(s) - 3]
    c = s[len(s) - 3 : ]
    if check(b) and c == '.py':
        print("yes")
    else: print("no")
    