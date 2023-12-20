def main():
    lines = readLines("input.txt")

    startPoints = []
    for c in range(len(lines[0])):
        startPoints.append((0, c, "D"))
        startPoints.append((len(lines) - 1, c, "U"))
    for r in range(len(lines)):
        startPoints.append((r, 0, "R"))
        startPoints.append((r, len(lines[0]) - 1, "L"))

    acc = 0
    for s in startPoints:
        todo = {s}
        marked = set()
        while len(todo) > 0:
            r, c, dir = todo.pop()
            if (r, c, dir) in marked:
                continue
            if r < 0 or r >= len(lines) or c < 0 or c >= len(lines[0]):
                continue

            marked.add((r, c, dir))
            cell = lines[r][c]
            if dir == "R":
                if cell == ".":
                    todo.add((r, c + 1, "R"))
                elif cell == "/":
                    todo.add((r - 1, c, "U"))
                elif cell == "\\":
                    todo.add((r + 1, c, "D"))
                elif cell == "|":
                    todo.add((r - 1, c, "U"))
                    todo.add((r + 1, c, "D"))
                elif cell == "-":
                    todo.add((r, c + 1, "R"))
                else:
                    raise ""
            elif dir == "D":
                if cell == ".":
                    todo.add((r + 1, c, "D"))
                elif cell == "/":
                    todo.add((r, c - 1, "L"))
                elif cell == "\\":
                    todo.add((r, c + 1, "R"))
                elif cell == "|":
                    todo.add((r + 1, c, "D"))
                elif cell == "-":
                    todo.add((r, c - 1, "L"))
                    todo.add((r, c + 1, "R"))
                else:
                    raise ""
            elif dir == "L":
                if cell == ".":
                    todo.add((r, c - 1, "L"))
                elif cell == "/":
                    todo.add((r + 1, c, "D"))
                elif cell == "\\":
                    todo.add((r - 1, c, "U"))
                elif cell == "|":
                    todo.add((r - 1, c, "U"))
                    todo.add((r + 1, c, "D"))
                elif cell == "-":
                    todo.add((r, c - 1, "L"))
                else:
                    raise ""
            elif dir == "U":
                if cell == ".":
                    todo.add((r - 1, c, "U"))
                elif cell == "/":
                    todo.add((r, c + 1, "R"))
                elif cell == "\\":
                    todo.add((r, c - 1, "L"))
                elif cell == "|":
                    todo.add((r - 1, c, "U"))
                elif cell == "-":
                    todo.add((r, c - 1, "L"))
                    todo.add((r, c + 1, "R"))
                else:
                    raise ""
            else:
                raise ""

        marked2 = set()
        for p in marked:
            marked2.add((p[0], p[1]))
        res = len(marked2)
        if res > acc:
            acc = res

    print(acc)
def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
