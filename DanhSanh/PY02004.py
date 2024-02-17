





if __name__ == '__main__':
    n, s, ans = int(input()),input().split(), 0
    cnt = 0
    for i in range(0, len(s)- 1):
        if s[i] != s[i + 1]:
            cnt += 1
    print(cnt)

