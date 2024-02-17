# F[i] = F[i - 1] + a[i] 
# tính tổng từ l - r : F[r] - F[l - 1], trường hợp 0 - r thì sum = F[r]

F = [0] * 10 # n = 10
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
F[0] = list[0]
for i in range(1, 10):
    F[i] = F[i - 1] + list[i]

print(F[5] - F[2])  # Tính Tổng Từ vị Trí 3 Đến 5
print(F[1])
