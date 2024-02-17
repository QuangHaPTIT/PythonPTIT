




from collections import Counter
from functools import cmp_to_key
def cmp(a, b):
    if a[0][1] != b[0][1]:
        return b[0][1] - a[0][1]
    else:
        return a[0][0] - b[0][0]

if __name__ == '__main__':
    m, n = map(int, input().split())
    ls = list(map(int, input().split()))
    lsc = list(dict(Counter(ls)).items())
    lsc.sort(key= lambda x : (-x[1], x[0]))
    st = set()
    for i in range(len(lsc)):
        st.add(lsc[i][1])
    if len(st) == 1:
        print("NONE")
    else:
        for i in range(len(lsc)):
            if lsc[i][1] != lsc[0][1]:
                print(lsc[i][0])
                break