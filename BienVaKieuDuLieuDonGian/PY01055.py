








def check(a):
    if len(a) % 2 == 0:
        return False
    if a[0] == a[1]:
        return False
    for i in range(0, len(a) - 2, 2):
        if a[i] != a[i + 2]:
            return False
    if (a[0] != a[len(a) - 1]):
        return False
    return True



if __name__ == '__main__':
    for t in range(int(input())):
        s = input()
        if check(s):
            print("YES")
        else:
            print("NO")