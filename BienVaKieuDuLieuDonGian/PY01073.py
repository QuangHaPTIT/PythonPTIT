

from itertools import  permutations


if __name__ == '__main__':
    s = input()
    permutations_list = list(permutations(s))
    for permu in permutations_list:
        print(*permu, sep="")
