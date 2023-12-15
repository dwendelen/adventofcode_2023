def main():
    lines = readLines("input.txt")

    expanded = transpose(expand(transpose(expand(lines))))

    points = []
    for l, line in enumerate(expanded):
        for c, item in enumerate(line):
            if item == "#":
                points.append((l, c))

    acc = 0
    for p, point1 in enumerate(points):
        for point2 in points[p + 1:]:
            acc += abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    print(acc)

def expand(list):
    acc = []
    for row in list:
        empty = True
        for r in row:
            if r != ".":
                empty = False
                break
        if empty:
            acc.append(row)
            acc.append(row)
        else:
            acc.append(row)
    return acc

def transpose(list):
    ll = len(list)
    cc = len(list[0])

    acc = []
    for c in range(cc):
        row = []
        for l in range(ll):
            row.append(list[l][c])
        acc.append(row)
    return acc
def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
