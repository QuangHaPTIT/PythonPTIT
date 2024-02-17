








import re

def print_consecutive_numbers(string):
    numbers = re.findall(r'\d+', string)
    consecutive_numbers = [num for num in numbers if len(num) >= 1]
    ls = list(map(int, consecutive_numbers))
    print(min(ls))

# Chuỗi đầu vào


# In ra các số liên tiếp trong chuỗi

if __name__ == '__main__':
    for t in range(int(input())):
        print_consecutive_numbers(input())