def main():
    lines = readLines("input.txt")
    # 760 is too high
    # 549 is too high

    bricks = []
    for line in lines:
        points = line.split("~")
        point1 = points[0].split(",")
        point2 = points[1].split(",")
        bricks.append((
            (int(point1[0]), int(point2[0])),
            (int(point1[1]), int(point2[1])),
            (int(point1[2]), int(point2[2]))
        ))

    supports = []
    isSupportedBy = []

    heightMap = []
    topBrick = []
    for x in range(1000):
        acc1 = []
        acc2 = []
        for y in range(1000):
            acc1.append(0)
            acc2.append(-1)
        heightMap.append(acc1)
        topBrick.append(acc2)

    bricks.sort(key=lambda e: e[2][0])
    for i, brick in enumerate(bricks):
        maxHeight = 0
        support = []
        for x in range(brick[0][0], brick[0][1] + 1):
            for y in range(brick[1][0], brick[1][1] + 1):
                h = heightMap[x][y]
                top = topBrick[x][y]
                if h == maxHeight and top != -1:
                    if top not in support:
                        support.append(top)
                elif h > maxHeight:
                    maxHeight = h
                    if top == -1:
                        support = []
                    else:
                        support = [top]
        isSupportedBy.append(support)
        for sup in support:
            ss = supports[sup]
            if i not in ss:
                ss.append(i)
            else:
                pass
        supports.append([])

        for x in range(brick[0][0], brick[0][1] + 1):
            for y in range(brick[1][0], brick[1][1] + 1):
                heightMap[x][y] = maxHeight + (brick[2][1] - brick[2][0] + 1)
                topBrick[x][y] = i


    # fall [ if I drop this one ] [ will this one drop ]
    fall = []
    todo = set()
    for i in range(len(bricks)):
        todo.add((i, i))
        acc = []
        for j in range(len(bricks)):
                acc.append(False)
        fall.append(acc)

    while len(todo) > 0:
        brick, source = todo.pop()
        if not fall[source][brick]:
            fall[source][brick] = True
            for sup in supports[brick]:
                willFall = True
                for s in isSupportedBy[sup]:
                    if not fall[source][s]:
                        willFall = False
                        break
                if willFall:
                    todo.add((sup, source))

    acc = -len(bricks)
    for i in fall:
        for j in i:
            if j:
                acc += 1

    print(acc)

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
