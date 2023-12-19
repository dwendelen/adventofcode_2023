def main():
    lines = readLines("input.txt")
    target = 1000000000

    grid = lines

    known = {}
    cyclesDone = 0
    cycles1 = -1
    cycles2 = -1
    while True:
        for _ in range(4):
            grid = tiltNorthAndRotateRight(grid)
        cyclesDone += 1
        asTuple = tuple(map(lambda e: tuple(e), grid))

        if asTuple in known:
            cycles1 = known[asTuple]
            cycles2 = cyclesDone
            break
        else:
            known[asTuple] = cyclesDone

    cyclesLeft = (target - cycles1) % (cycles2 - cycles1)

    for _ in range(cyclesLeft):
        for _ in range(4):
            grid = tiltNorthAndRotateRight(grid)

    acc = 0
    max = len(grid)
    for c in range(len(grid[0])):
        for r in range(len(lines)):
            item = grid[r][c]
            if item == "O":
                acc += max - r

    print(acc)




def tiltNorthAndRotateRight(grid):
    rows = len(grid)
    cols = len(grid[0])

    nextGrid = []
    acc = []
    for r in range(cols):
        for c in range(rows):
            acc.append(".")
        nextGrid.append(acc)
        acc = []


    for c in range(len(grid[0])):
        nextPos = 0
        for r in range(len(grid)):
            item = grid[r][c]
            if item == "O":
                nextGrid[c][cols - nextPos - 1] = "O"
                nextPos += 1
            elif item == "#":
                nextGrid[c][cols - r - 1] = "#"
                nextPos = r + 1

    return nextGrid

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
