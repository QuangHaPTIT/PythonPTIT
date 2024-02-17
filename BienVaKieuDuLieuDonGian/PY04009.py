if __name__ == '__main__':
    for _ in range(int(input())):
        l = list(map(int, input().split()))
        a = complex(l[0], l[1])
        b = complex(l[2], l[3])
        c = (a + b) * a
        d = (a + b) * (a + b)
        if c.imag >= 0: print(f"{int(c.real)} + {int(c.imag)}i, ", end = "")
        else: print(f"{int(c.real)} - {-int(c.imag)}i, ", end = "")
        if d.imag > 0: print(f"{int(d.real)} + {int(d.imag)}i")
        else: print(f"{int(d.real)} - {-int(d.imag)}i")