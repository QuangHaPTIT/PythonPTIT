








class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao
    def __add__(self, other):
        tmp1 = self.thuc + other.thuc
        tmp2 = self.ao + other.ao
        return SoPhuc(tmp1, tmp2)
    def __sub__(self, other):
        tmp1 = self.thuc - other.thuc
        tmp2 = self.ao - other.ao
        return SoPhuc(tmp1, tmp2)
    def __mul__(self, other):
        tmp1 = (self.thuc * other.thuc - other.ao * other.ao)
        tmp2 = (self.thuc * other.ao + other.thuc * self.ao)
        return SoPhuc(tmp1, tmp2)
    def __str__(self):
        return f'{self.thuc} + {self.ao}j'


if __name__ == '__main__':
    s1 = SoPhuc(3, 2)
    s2 = SoPhuc(3, 1)
    s3 = s1 + s2
    s4 = s1 - s2
    s5 = s1 * s2
    print(s3)
    print(s4)
    print(s5)