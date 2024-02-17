







gt = [0] * 10
gt[0] = 1
gt[1] = 1
def gt_1_9():
    global gt
    for i in range(2, 10, 1):
        gt[i] = gt[i - 1] * i

def sum_degit_gt(n):
    sum = 0
    while n != 0:
        sum += gt[n % 10]
        n //= 10
    return sum
if __name__ == '__main__':
    gt_1_9()
    for t in range(int(input())):
        n = int(input())
        if sum_degit_gt(n) == n:
            print("Yes")
        else:
            print("No")