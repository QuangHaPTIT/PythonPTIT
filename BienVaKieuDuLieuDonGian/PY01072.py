from itertools import combinations


if __name__ == '__main__':
    n, k = map(int, input().split())
    ls = sorted(list({int(x) for x in input().split()}))
    t = tuple(int(x) for x in range(1, len(ls) + 1))
    
    combinations_list = list(combinations(t, k))
    for combi in combinations_list:
        for j in combi:
            print(ls[j - 1], end= " ")
        print()
    