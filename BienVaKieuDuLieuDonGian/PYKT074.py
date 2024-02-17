import textwrap





if __name__ == '__main__':
    for t in range(int(input())):
        print(textwrap.shorten(input(), width=100, placeholder=''))