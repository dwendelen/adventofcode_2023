def main():
    lines = readLines("input.txt")
    cards = split_list(lines, "")

    cols = 0
    rows = 0
    for card in cards:
        for c in range(1, len(card[0])):
            width = min(c, len(card[0]) - c)
            matches = True
            for cc in range(width):
                c1 = c + cc
                c2 = c - cc - 1

                for r in range(len(card)):
                    if card[r][c1] != card[r][c2]:
                        matches = False
            if matches:
                cols += c

        for r in range(1, len(card)):
            height = min(r, len(card) - r)
            matches = True
            for rr in range(height):
                r1 = r + rr
                r2 = r - rr - 1

                for c in range(len(card[0])):
                    if card[r1][c] != card[r2][c]:
                        matches = False
            if matches:
                rows += r

    res = 100 * rows + cols
    print(res)




def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

def split_list(list, delim):
    acc = []
    subAcc = []
    for item in list:
        if item == delim:
            if subAcc != []:
                acc.append(subAcc)
            subAcc = []
        else:
            subAcc.append(item)
    if subAcc != []:
        acc.append(subAcc)
    return acc

main()
