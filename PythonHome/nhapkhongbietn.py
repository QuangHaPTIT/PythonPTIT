# Mảng chẵn lẻ

from sys import stdin # Dùng để đọc luồng đầu vào khi không biết n




if __name__ == '__main__':
    a = []
    for s in stdin:
        a += list(map(int, input().split()))
    print(a)