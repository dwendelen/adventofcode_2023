def main():
    lines = readLines("input.txt")

    acc = 0
    max = len(lines)
    for c in range(len(lines[0])):
        nextPos = 0
        for r in range(len(lines)):
            item = lines[r][c]
            if item == "O":
                acc += max - nextPos
                nextPos += 1
            elif item == "#":
                nextPos = r + 1

    print(acc)






def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
