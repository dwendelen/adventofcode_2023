def main():
    lines = readLines("input.txt")

    def s(line):
        return list(map(int, line.split(" ")))

    sequences = list(map(s, lines))

    acc = 0
    for s in sequences:
        acc += solve(s)

    print(acc)

def solve(sequence):
    sub = []
    prev = sequence[0]
    for s in sequence[1:]:
        sub.append(s - prev)
        prev = s

    if prev == 0:
        return 0
    else:
        n = solve(sub)
        return sequence[0] - n
def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
