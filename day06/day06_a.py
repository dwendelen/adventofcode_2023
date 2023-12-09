import re

def main():
    lines = readLines("input.txt")
    times = map(lambda e: int(e.strip()), filter(lambda e: e != "", lines[0][9:].split(" ")))
    distances = list(map(lambda e: int(e.strip()), filter(lambda e: e != "", lines[1][9:].split(" "))))

    races = []
    for i, time in enumerate(times):
        races.append(Race(time, distances[i]))

    acc = 1
    for race in races:
        acc *= race.solve()

    print(acc)

class Race:
    def __init__(self, time, distance):
        self.time = time
        self.distance = distance

    def solve(self):
        cnt = 0
        for t in range(self.time):
            myDist = (self.time - t) * t
            if myDist > self.distance:
                cnt += 1
        return cnt

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
