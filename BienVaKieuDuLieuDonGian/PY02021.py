









if __name__ == '__main__':
    for t in range(int(input())):
        n, m, g = map(int, input().split())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = list(map(int, input().split()))
        i, j, k = 0, 0, 0
        ok = False
        while i < n and j < m and k < g:
            if a[i] == b[j] and b[j] == c[k]:
                print(a[i], end=" ")
                i += 1
                j += 1
                k += 1
                ok = True
            else:
                if a[i] < b[j]:
                    i += 1
                elif b[j] < c[k]:
                    j += 1
                elif c[k] < a[i]:
                    k += 1
        if not ok:
            print("NO")
        else: print()
