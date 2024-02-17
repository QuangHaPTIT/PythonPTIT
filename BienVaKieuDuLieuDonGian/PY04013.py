from datetime import *
class Station:
    next_id = 1
    def __init__(self, name, start, end, rainfall):
        self.id = f"T{Station.next_id:02d}"
        Station.next_id += 1
        self.name = name
        time_format = "%H:%M"
        time_start = datetime.strptime(start, time_format)
        time_end = datetime.strptime(end, time_format)
        self.time = (time_end - time_start).total_seconds()
        self.rainfall = rainfall

    def update(self, start, end, rainfall):
        time_format = "%H:%M"
        time_start = datetime.strptime(start, time_format)
        time_end = datetime.strptime(end, time_format)
        self.time += (time_end - time_start).total_seconds()
        self.rainfall += rainfall

    def __str__(self):
        return self.id + " " + self.name + " " + (f"%.2f" % (d[x].rainfall * 3600 / d[x].time))

if __name__ == '__main__':
    d = {}
    for _ in range(int(input())):
        name = input()
        start = input()
        end = input()
        rainfall = int(input())
        if name in d: d[name].update(start, end, rainfall)
        else: d[name] = Station(name, start, end, rainfall)
    for x in d: print(d[x])