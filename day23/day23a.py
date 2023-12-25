def main():
    lines = readLines("input.txt")

    start = (0, 1)
    end = (len(lines) - 1, len(lines[0]) - 2)
    queue = [(start, 0, {start})]

    acc = 0
    while len(queue) != 0:
        pos, dist, visited = queue.pop()
        if pos == end:
            if acc < dist:
                acc = dist
        else:
            maybeDirs = (
                (pos[0] - 1, pos[1], "^"),
                (pos[0] + 1, pos[1], "v"),
                (pos[0], pos[1] - 1, "<"),
                (pos[0], pos[1] + 1, ">")
            )
            for newPos in maybeDirs:
                char = lines[newPos[0]][newPos[1]]
                posPos = (newPos[0], newPos[1])
                if (char == "." or char == newPos[2]) and posPos not in visited:
                    newVisited = visited.copy()
                    newVisited.add(posPos)
                    queue.append((posPos, dist + 1, newVisited))

    print(acc)

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
