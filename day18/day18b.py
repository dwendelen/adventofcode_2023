from binascii import b2a_hex

def main():
    lines = readLines("input.txt")

    curr = (0, 0)
    triangle = 0
    len = 0

    for line in lines:
        pieces = line.split(" ")
        cnt = int(pieces[2][2:7], 16)
        dir = pieces[2][7]
        # 0 R, 1 D, 2 L, 3 U
        if dir == "3":  # U
            diff = (-1, 0)
            triangle += curr[1] * cnt
        elif dir == "1":  # D
            diff = (1, 0)
            triangle -= curr[1] * cnt
        elif dir == "2":  # L
            diff = (0, -1)
            triangle -= curr[0] * cnt
        elif dir == "0":  # R
            diff = (0, 1)
            triangle += curr[0] * cnt
        else:
            raise "error"
        len += cnt
        curr = (curr[0] + diff[0] * cnt, curr[1] + diff[1] * cnt)

    # We add half the length and plus two, because our path creates a trench, it's not a line
    area = abs(triangle // 2) + len // 2 + 1
    print(abs(area))

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()