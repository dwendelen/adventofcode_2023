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

    while curr != start:
        if prev == "T":
            if lines[curr[0]][curr[1]] == "|":
                curr = (curr[0] + 1, curr[1])
                prev = "T"
            elif lines[curr[0]][curr[1]] == "L":
                curr = (curr[0], curr[1] + 1)
                prev = "L"
            elif lines[curr[0]][curr[1]] == "J":
                curr = (curr[0], curr[1] - 1)
                prev = "R"
            else:
                raise "Error"
        elif prev == "R":
            if lines[curr[0]][curr[1]] == "-":
                curr = (curr[0], curr[1] - 1)
                prev = "R"
            elif lines[curr[0]][curr[1]] == "L":
                curr = (curr[0] - 1, curr[1])
                prev = "B"
            elif lines[curr[0]][curr[1]] == "F":
                curr = (curr[0] + 1, curr[1])
                prev = "T"
            else:
                raise "Error"
        elif prev == "B":
            if lines[curr[0]][curr[1]] == "|":
                curr = (curr[0] - 1, curr[1])
                prev = "B"
            elif lines[curr[0]][curr[1]] == "7":
                curr = (curr[0], curr[1] - 1)
                prev = "R"
            elif lines[curr[0]][curr[1]] == "F":
                curr = (curr[0], curr[1] + 1)
                prev = "L"
            else:
                raise "Error"
        elif prev == "L":
            if lines[curr[0]][curr[1]] == "-":
                curr = (curr[0], curr[1] + 1)
                prev = "L"
            elif lines[curr[0]][curr[1]] == "7":
                curr = (curr[0] + 1, curr[1])
                prev = "T"
            elif lines[curr[0]][curr[1]] == "J":
                curr = (curr[0] - 1, curr[1])
                prev = "B"
            else:
                raise "Error"
        else:
            raise "Error"
        acc += 1

    print(acc)
    print(acc//2)
def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
