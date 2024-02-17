














if __name__ == '__main__':
    
    n, ls = int(input()), list(map(int, input().split()))
    st = []
    for i in ls:
        if len(st) == 0:
            st.append(i)
        else:
            if (st[-1] + i) % 2 == 0:
                st.pop()
            else:
                st.append(i)
    print(len(st))

