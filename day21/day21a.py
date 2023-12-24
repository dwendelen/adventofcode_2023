def main():
    lines = readLines("input.txt")
    # 256 too low
    steps = 64

    rows = len(lines)
    cols = len(lines[0])

    start = (-1, -1)
    for r, line in enumerate(lines):
        for c, char in enumerate(line):
            if char == "S":
                start = (r, c)

    wave = {start}

    for _ in range(steps):
        nextWave = set()
        for r, c in wave:
            maybePos = (
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1)
            )
            for nr, nc in maybePos:
                if 0 <= nr and nr < rows and 0 <= nc and nc < cols and lines[nr][nc] != "#":
                    nextWave.add((nr, nc))
        wave = nextWave

    res = len(wave)
    print(res)

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines


main()
