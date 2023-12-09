import re

def main():
    lines = readLines("input.txt")
    seeds = list(map(lambda i: int(i), lines[0].split(": ")[1].split(" ")))

    maps1 = split_list(lines[2:], "")
    maps2 = list(map(lambda i: Map(list(map(lambda j: Range(int(j.split(" ")[0]), int(j.split(" ")[1]), int(j.split(" ")[2])), i[1:]))), maps1))

    prev = maps2[0]
    for m in maps2[1:]:
        prev.next = m
        prev = m

    min = 999999999999999999999999999999999

    for i in range(len(seeds) // 2):
        pos = seeds[2 * i]
        dist = seeds[2 * i + 1]
        myMin = maps2[0].min(pos, pos + dist)
        if myMin < min:
            min = myMin

    print(min)

class Map:
    next = None

    def __init__(self, ranges):
        def start(r):
            return r.start

        ranges.sort(key=start)
        self.ranges = []
        prev = Range(0, 0, 0)
        for range in ranges:
            if range.start != prev.end:
                self.ranges.append(Range(prev.end, prev.end, range.start - prev.end))
            self.ranges.append(range)
            prev = range
        self.ranges.append(Range(self.ranges[-1].end, self.ranges[-1].end, 99999999999999999999999))
        print()


    def min(self, start, end):
        myMin = 99999999999999999999999999999
        for range in self.ranges:
            mapped = range.map(start, end)
            if mapped != None:
                if self.next == None:
                    res = mapped[0]
                else:
                    res = self.next.min(mapped[0], mapped[1])

                if res < myMin:
                    myMin = res

        return myMin

class Range:
    def __init__(self, dest, source, range):
        self.dest = dest
        self.start = source
        self.end = source + range

    def map(self, start, end):
        start1 = max(self.start, start)
        end1 = min(self.end, end)

        if start1 < end1:
            return (start1 - self.start + self.dest, end1 - self.start + self.dest)
        else:
            None

def split_list(list, delim):
    acc = []
    subAcc = []
    for item in list:
        if item == delim:
            if subAcc != []:
                acc.append(subAcc)
            subAcc = []
        else:
            subAcc.append(item)
    if subAcc != []:
        acc.append(subAcc)
    return acc


def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
