def main():
    # 26501365 mod 131 is 65
    # -> up, down, left, right 130 steps
    # There are two full pattern, which we will call odd and even
    # Adjacent grids have opposite pattern because the grid is 131
    # We will assume the start is odd
    #
    #      1 U 1
    #    1 2 O 2 1
    #  1 2 O E O 2 1
    #  L O E O E O R
    #  1 2 O E O 2 1
    #    1 2 O 2 1
    #      1 D 1
    #
    # jumps = 1:  1 O +  4 E +  4 2 +  8 1      17
    #             + 8           + 4    + 4     +16
    # jumps = 2:  9 O +  4 E +  8 2 + 12 1      33
    #                   + 12    + 4    + 4     +20
    # jumps = 3:  9 O + 16 E + 12 2 + 16 1      53
    #            + 16           + 4    + 4     +24
    # jumps = 4: 25 O + 16 E + 16 2 + 20 1      77
    #                   + 20    + 4    + 4     +28
    # jumps = 5: 25 O + 36 E + 20 2 + 24 1     105
    #            + 24           + 4    + 4     +28
    # jumps = 6: 49 O + 36 E + 24 2 + 28 1     137
    #
    # n_1(j) = (j + 1) * 4
    # n_2(j) = j * 4
    # n_e(j) = n_e(j - 2) + n_2(j - 1) + 4
    # n_e(j) = n_e(j - 2) + (j - 1) * 4 + 4
    # n_e(j) = n_e(j - 2) + j * 4
    # n_e(j) = (j + 1 // 2) * (j + 1 // 2) * 4
    # n_e(j) = (2 * ((j + 1) // 2)) * (2 * ((j + 1) // 2))
    # n_o(j) = n_o(j - 2) + n_2(j - 1) + 4
    # n_o(j) = n_o(j - 2) + (j - 1)*4 + 4
    # n_o(j) = n_o(j - 2) + j * 4
    # n_o(j) = ((j // 2) + 1) * ((j // 2) + 1) * 4
    # n_o(j) = ( 2 * (j // 2) + 1) * (2 * (j // 2) + 1)

    lines = readLines("input.txt")
    steps = 26501365
    # 619409683163967 is too high
    # 619405080647882 is too low

    rows = len(lines)
    cols = len(lines[0])

    straightSteps = (steps - 66) % 131
    diagonalSteps1 = (steps - 66 - 66) % 131
    diagonalSteps2 = diagonalSteps1 + 131

    odd = simulate(lines, rows, cols, (65, 65), 131)
    even = simulate(lines, rows, cols, (65, 65), 132)
    up = simulate(lines, rows, cols, (130, 65), straightSteps)
    down = simulate(lines, rows, cols, (0, 65), straightSteps)
    left = simulate(lines, rows, cols, (65, 130), straightSteps)
    right = simulate(lines, rows, cols, (65, 0), straightSteps)

    upRight1 = simulate(lines, rows, cols, (130, 0), diagonalSteps1)
    upRight2 = simulate(lines, rows, cols, (130, 0), diagonalSteps2)
    downRight1 = simulate(lines, rows, cols, (0, 0), diagonalSteps1)
    downRight2 = simulate(lines, rows, cols, (0, 0), diagonalSteps2)
    downLeft1 = simulate(lines, rows, cols, (0, 130), diagonalSteps1)
    downLeft2 = simulate(lines, rows, cols, (0, 130), diagonalSteps2)
    upLeft1 = simulate(lines, rows, cols, (130, 130), diagonalSteps1)
    upLeft2 = simulate(lines, rows, cols, (130, 130), diagonalSteps2)

    jumps = (steps - 66) // 131
    even_jumps = (2 * ((jumps + 1) // 2))
    odd_jumps = (2 * (jumps // 2) + 1)
    n_even = even_jumps * even_jumps
    n_odd = odd_jumps * odd_jumps
    n_1 = (jumps + 1)  # divided by 4
    n_2 = jumps  # divided by 4

    res = even * n_even + \
          odd * n_odd + \
          n_1 * (upRight1 + downRight1 + downLeft1 + upLeft1) + \
          n_2 * (upRight2 + downRight2 + downLeft2 + upLeft2) + \
          up + down + left + right

    print(res)

def simulate(lines, rows, cols, start, steps):
    wave = {start}
    for s in range(steps):
        nextWave = set()
        for r, c in wave:
            maybePos = (
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1)
            )
            for nr, nc in maybePos:
                if 0 <= nr < rows and 0 <= nc < cols and lines[nr][nc] != "#":
                    nextWave.add((nr, nc))
        wave = nextWave

    return len(wave)


def printGrid(lines, rows, cols, wave):
    print()

    acc = "     "
    prev = 0
    for c in range(cols):
        char = c // 100
        if char != prev:
            acc += str(char)
        else:
            acc += " "
        prev = char
    print(acc)

    acc = "     "
    prev = 0
    for c in range(cols):
        char = (c % 100) // 10
        if char != prev:
            acc += str(char)
        else:
            acc += " "
        prev = char
    print(acc)

    acc = "     "
    for c in range(cols):
        char = c % 10
        acc += str(char)
    print(acc)

    print()

    for r in range(rows):
        acc = str(r).rjust(3, " ") + "  "
        for c in range(cols):
            if (r, c) in wave:
                acc += "O"
            elif lines[r][c] == "#":
                acc += "#"
            else:
                acc += "."
        print(acc)
    print()


def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines


main()
