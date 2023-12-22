from queue import PriorityQueue

def main():
    map = readLines("input.txt")

    rows = len(map)
    cols = len(map[0])
    dest = (rows - 1, cols - 1)

    queue = PriorityQueue()
    queue.put((0, 0, 0, 5, "X"))
    best = {(0, 0, 5, "X"): 0}

    res = None
    while(True):
        item = queue.get(False)
        loss, row, col, cnt, dir = item

        if dest == (row, col) and cnt >= 4:
            res = loss
            break

        if dir == "X":
            maybeDirs = (
                (row + 1, col, "D"),
                (row, col + 1, "R")
            )
        elif dir == "U":
            maybeDirs = (
                (row - 1, col, "U"),
                (row, col - 1, "L"),
                (row, col + 1, "R")
            )
        elif dir == "D":
            maybeDirs = (
                (row + 1, col, "D"),
                (row, col - 1, "L"),
                (row, col + 1, "R")
            )
        elif dir == "L":
            maybeDirs = (
                (row - 1, col, "U"),
                (row + 1, col, "D"),
                (row, col - 1, "L"),
            )
        elif dir == "R":
            maybeDirs = (
                (row - 1, col, "U"),
                (row + 1, col, "D"),
                (row, col + 1, "R"),
            )
        else:
            raise "error"

        for d in maybeDirs:
            if d[0] < 0 or d[0] >= rows or d[1] < 0 or d[1] >= cols:
                continue
            if d[2] == dir and cnt == 10:
                continue
            if d[2] != dir and cnt < 4:
                continue
            addLoss = int(map[d[0]][d[1]])
            newLoss = loss + addLoss
            if d[2] == dir:
                newCnt = cnt + 1
            else:
                newCnt = 1
            key = (d[0], d[1], newCnt, d[2])
            currentBest = best.get(key, 99999999999)
            if newLoss < currentBest:
                best[key] = newLoss
                queue.put((newLoss, d[0], d[1], newCnt, d[2]), False)

    print(res)

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
