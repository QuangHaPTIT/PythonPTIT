












if __name__ == '__main__':
    f = open("input.txt", "r")
    s1, s2 = input().split(), input().split()
    u, s = set(s1), set(s2)
    print(*(sorted(u.union(s))), sep=" ")
    print(*(sorted(u.intersection(s))), sep=" ")
