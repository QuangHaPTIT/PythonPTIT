import math

class Fract:
    def __init__(self, tu, mau):
        self.tu, self.mau = tu, mau
    def rutGon(self):
        GCD = math.gcd(self.tu, self.mau)
        self.tu //= GCD
        self.mau //= GCD
        return "{}/{}".format(self.tu, self.mau)

t, m = list(map(int, input().split()))
A = Fract(t, m)
print(A.rutGon())