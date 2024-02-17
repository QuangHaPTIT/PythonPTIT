class Gamer:
    def __init__(self, id, name, time_in, time_out):
        self.id = id
        self.name = name
        self.time_in = time_in
        self.time_out = time_out
        self.calculate_time()

    def calculate_time(self):
        i = int(self.time_in[0:2]) * 60 + int(self.time_in[3:])
        o = int(self.time_out[0:2]) * 60 + int(self.time_out[3:])
        self.time = o - i

    def time_str(self):
        return '{} gio {} phut'.format(self.time // 60, self.time % 60)

    def __str__(self):
        return '{} {} {}'.format(self.id, self.name, self.time_str())
if __name__ == '__main__':
    l = []
    for i in range(int(input())):
        l.append(Gamer(input(), input(), input(), input()))
    l.sort(key=lambda e: (-e.time))
    print(*l, sep='\n')