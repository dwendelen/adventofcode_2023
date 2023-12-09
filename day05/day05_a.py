import re

def main():
    lines = readLines("input.txt")
    seeds = map(lambda i: int(i), lines[0].split(": ")[1].split(" "))

    maps1 = split_list(lines[2:], "")
    maps2 = map(lambda i: list(map(lambda j: Range(int(j.split(" ")[0]), int(j.split(" ")[1]), int(j.split(" ")[2])), i[1:])), maps1)
    maps3 = list(maps2)

    min = 999999999999999999999999999999999
    for seed in seeds:
        loc = resolve(maps3, seed)
        if loc < min:
            min = loc

    print(min)

def resolve(maps, seed):
    acc = seed
    for map in maps:
        acc = resolveMap(map, acc)
    return acc

def resolveMap(map, source):
    for range in map:
        mapped = range.map(source)
        if mapped != None:
            return mapped
    return source


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

class Range:
    def __init__(self, dest, source, range):
        self.dest = dest
        self.source = source
        self.range = range

    def map(self, num):
        if num >= self.source and num < self.source + self.range:
            return num - self.source + self.dest
        else:
            None

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
