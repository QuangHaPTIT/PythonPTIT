







if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0: break
        st = set({})
        
        m = 0
        m2 = 9999999999999999999999999999999999999999
        for i in range(n):
            k = int(input())
            st.add(k)
            if k > m:
                m = k
            if m2 > k:
                m2 = k
        if len(st) == 1:
            print("BANG NHAU")
        else:
            print(m2, m)