import re

def main():
    acc = 0
    lines = readLines("input.txt")
    for l, line in enumerate(lines):
        num = 0
        isPart = False
        for c, char in enumerate(line):
            if char.isdigit():
                num = 10 * num + int(char)
                if part(lines, l, c):
                    isPart = True
            else:
                if isPart:
                    acc += num
                num = 0
                isPart = False
        if isPart:
            acc += num
    print(acc)

def part(lines, l, c):
    friends = [
        (l - 1, c - 1), (l - 1, c), (l - 1, c + 1),
        (l, c - 1), (l, c + 1),
        (l + 1, c - 1), (l + 1, c), (l + 1, c + 1)
    ]
    for f in friends:
        if f[0] >= 0 and f[0] < len(lines) and f[1] >= 0 and f[1] < len(lines[0]):
            char = lines[f[0]][f[1]]
            if not char.isdigit() and not char == '.':
                return True
    return False

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
