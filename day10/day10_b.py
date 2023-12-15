# |    L       J   7 7   F F
# |    L L   J J     7   F
# - -

#   T
# L   R
#   B

def main():
    lines = readLines("input.txt")

    start = None
    for l, line in enumerate(lines):
        for c, item in enumerate(line):
            if item == "S":
                start = (l, c)

    curr = None
    prev = None
    acc = 1

    if lines[start[0] - 1][start[1]] == "|" \
        or lines[start[0] - 1][start[1]] == "7" \
        or lines[start[0] - 1][start[1]] == "F":
            curr = (start[0] - 1, start[1])
            prev = "B"
    elif lines[start[0]][start[1] + 1] == "-" \
        or lines[start[0]][start[1] + 1] == "7" \
        or lines[start[0]][start[1] + 1] == "J":
            curr = (start[0], start[1] + 1)
            prev = "L"
    elif lines[start[0] + 1][start[1]] == "|" \
        or lines[start[0] + 1][start[1]] == "J" \
        or lines[start[0] + 1][start[1]] == "L":
            curr = (start[0] + 1, start[1])
            prev = "T"


    leftTurns = 0
    rightTurns = 0

    path = {start}
    inner = set()
    todoLeft = set()
    todoRight = set()

    while curr != start:
        path.add(curr)
        if prev == "T":
            if lines[curr[0]][curr[1]] == "|":
                todoLeft.add((curr[0], curr[1] + 1))
                todoRight.add((curr[0], curr[1] - 1))
                curr = (curr[0] + 1, curr[1])
                prev = "T"
            elif lines[curr[0]][curr[1]] == "L":
                leftTurns += 1
                todoRight.add((curr[0], curr[1] - 1))
                todoRight.add((curr[0] + 1, curr[1]))
                curr = (curr[0], curr[1] + 1)
                prev = "L"
            elif lines[curr[0]][curr[1]] == "J":
                rightTurns += 1
                todoLeft.add((curr[0], curr[1] + 1))
                todoLeft.add((curr[0] + 1, curr[1]))
                curr = (curr[0], curr[1] - 1)
                prev = "R"
            else:
                raise "Error"
        elif prev == "R":
            if lines[curr[0]][curr[1]] == "-":
                todoLeft.add((curr[0] + 1, curr[1]))
                todoRight.add((curr[0] - 1, curr[1]))
                curr = (curr[0], curr[1] - 1)
                prev = "R"
            elif lines[curr[0]][curr[1]] == "L":
                todoLeft.add((curr[0], curr[1] - 1))
                todoLeft.add((curr[0] + 1, curr[1]))
                curr = (curr[0] - 1, curr[1])
                prev = "B"
                rightTurns += 1
            elif lines[curr[0]][curr[1]] == "F":
                leftTurns += 1
                todoRight.add((curr[0], curr[1] - 1))
                todoRight.add((curr[0] - 1, curr[1]))
                curr = (curr[0] + 1, curr[1])
                prev = "T"
            else:
                raise "Error"
        elif prev == "B":
            if lines[curr[0]][curr[1]] == "|":
                todoLeft.add((curr[0], curr[1] - 1))
                todoRight.add((curr[0], curr[1] + 1))
                curr = (curr[0] - 1, curr[1])
                prev = "B"
            elif lines[curr[0]][curr[1]] == "7":
                leftTurns += 1
                todoRight.add((curr[0], curr[1] + 1))
                todoRight.add((curr[0] - 1, curr[1]))
                curr = (curr[0], curr[1] - 1)
                prev = "R"
            elif lines[curr[0]][curr[1]] == "F":
                rightTurns += 1
                todoLeft.add((curr[0], curr[1] - 1))
                todoLeft.add((curr[0] - 1, curr[1]))
                curr = (curr[0], curr[1] + 1)
                prev = "L"
            else:
                raise "Error"
        elif prev == "L":
            if lines[curr[0]][curr[1]] == "-":
                todoLeft.add((curr[0] - 1, curr[1]))
                todoRight.add((curr[0] + 1, curr[1]))
                curr = (curr[0], curr[1] + 1)
                prev = "L"
            elif lines[curr[0]][curr[1]] == "7":
                rightTurns += 1
                todoLeft.add((curr[0] - 1, curr[1]))
                todoLeft.add((curr[0], curr[1] + 1))
                curr = (curr[0] + 1, curr[1])
                prev = "T"
            elif lines[curr[0]][curr[1]] == "J":
                leftTurns += 1
                todoRight.add((curr[0], curr[1] + 1))
                todoRight.add((curr[0] + 1, curr[1]))
                curr = (curr[0] - 1, curr[1])
                prev = "B"
            else:
                raise "Error"
        else:
            raise "Error"
        acc += 1

    if leftTurns > rightTurns:
        todo = todoLeft
    else:
        todo = todoRight

    while len(todo) > 0:
        print(len(todo))
        item = next(iter(todo))
        todo.remove(item)
        if item in path or item in inner:
            continue
        else:
            inner.add(item)
            todo.add((item[0] - 1, item[1]))
            todo.add((item[0] + 1, item[1]))
            todo.add((item[0], item[1] - 1))
            todo.add((item[0], item[1] + 1))

    print(acc)
    print(acc//2)
    print(len(inner))
def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
