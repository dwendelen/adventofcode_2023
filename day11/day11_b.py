def main():
    lines = readLines("input.txt")
    gapSize = 1000000

    points = []

    colGaps = []
    rowGaps = []

    for l, row in enumerate(lines):
        empty = True
        for r in row:
            if r != ".":
                empty = False
                break
        if empty:
            rowGaps.append(l)

    for c in range(len(lines[0])):
        empty = True
        for line in lines:
            if line[c] != ".":
                empty = False
                break
        if empty:
            colGaps.append(c)

    extraRow = 0
    nextRowGap = rowGaps
    for l, line in enumerate(lines):
        if len(nextRowGap) > 0 and l > nextRowGap[0]:
            nextRowGap = nextRowGap[1:]
            extraRow += gapSize - 1
        extraCol = 0
        nextColGap = colGaps
        for c, item in enumerate(line):
            if len(nextColGap) > 0 and c > nextColGap[0]:
                nextColGap = nextColGap[1:]
                extraCol += gapSize - 1
            if item == "#":
                points.append((l + extraRow, c + extraCol))

    acc = 0
    for p, point1 in enumerate(points):
        for point2 in points[p + 1:]:
            acc += abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    print(acc)


def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
