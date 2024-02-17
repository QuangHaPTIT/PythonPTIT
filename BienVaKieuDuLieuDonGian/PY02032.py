







if __name__ == '__main__':
    s = input()
    st = set()
    for i in range(0, len(s), 2):
        x = (s[i:i + 2])
        if len(x) == 2:
            st.add(int(x))
    print(*sorted(st))
