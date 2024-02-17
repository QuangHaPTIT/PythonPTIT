
def check(s):
    if s[len(s) - 2] == '8' and s[len(s) - 1] == '6':
        return 'YES'
    else:
        return 'NO'
    



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        print(check(s))
        