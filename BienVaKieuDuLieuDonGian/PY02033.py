





from collections import Counter



if __name__ == '__main__':
    s = input()
    ls = list()
    for i in range(0, len(s), 2):
        x = s[i:i+2]
        if len(x) == 2:
            ls.append(int(x))
    
    ls = (dict(Counter(ls)))
    print(*ls.keys())