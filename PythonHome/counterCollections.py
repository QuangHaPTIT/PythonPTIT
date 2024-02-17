




from collections import Counter




if __name__ == '__main__':
    ls = [1, 2, 2, 5, 0, 0, 1, 4, 3]
    #b = Counter(list)
    b = list(dict(Counter(ls)).items())
    print(b)
    for i in range(len(b)):
        print(b[i][0], b[i][1], sep=" ")