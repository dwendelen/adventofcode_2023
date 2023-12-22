def main():
    lines = readLines("input.txt")
    randomInnerPoint = (-1, -3)

    curr = (0, 0)
    path = {(0, 0)}

    for line in lines:
        pieces = line.split(" ")
        if pieces[0] == "U":
            diff = (-1, 0)
        elif pieces[0] == "D":
            diff = (1, 0)
        elif pieces[0] == "L":
            diff = (0, -1)
        elif pieces[0] == "R":
            diff = (0, 1)
        else:
            raise "error"

        cnt = int(pieces[1])

        for _ in range(cnt):
            curr = (curr[0] + diff[0], curr[1] + diff[1])
            path.add(curr)

    inner = set()
    todo = {randomInnerPoint}

    while len(todo) > 0:
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

    print(len(inner) + len(path))

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()