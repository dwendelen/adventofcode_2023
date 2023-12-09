import re

def main():
    gears = {}
    lines = readLines("input.txt")
    for l, line in enumerate(lines):
        num = 0
        gear = None
        for c, char in enumerate(line):
            if char.isdigit():
                num = 10 * num + int(char)
                gearLoc = gearfn(lines, l, c)
                if gearLoc != None:
                    gear = gearLoc
            else:
                if gear != None:
                    newGearsValue = gears.get(gear, [])
                    newGearsValue.append(num)
                    gears[gear] = newGearsValue
                num = 0
                gear = None
        if gear != None:
            newGearsValue = gears.get(gear, [])
            newGearsValue.append(num)
            gears[gear] = newGearsValue
    acc = 0
    for gear in gears:
        if len(gears[gear]) == 2:
            acc += gears[gear][0] * gears[gear][1]
    print(acc)

def gearfn(lines, l, c):
    friends = [
        (l - 1, c - 1), (l - 1, c), (l - 1, c + 1),
        (l, c - 1), (l, c + 1),
        (l + 1, c - 1), (l + 1, c), (l + 1, c + 1)
    ]
    for f in friends:
        if f[0] >= 0 and f[0] < len(lines) and f[1] >= 0 and f[1] < len(lines[0]):
            char = lines[f[0]][f[1]]
            if char == '*':
                return f
    return None

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
