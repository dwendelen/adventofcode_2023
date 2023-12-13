def main():
    lines = readLines("input.txt")
    def p(e):
        if e == 'L':
            return 0
        else:
            return 1
    instr = list(map(p, lines[0]))
    nodes = {}
    for l in lines[2:]:
        id = l[0:3]
        left = l[7:10]
        right = l[12:15]
        nodes[id] = (left, right)

    acc = 0
    i = 0
    curr = "AAA"
    while curr != "ZZZ":
        if i >= len(instr):
            i = 0
        curr = nodes[curr][instr[i]]
        acc += 1
        i += 1

    print(acc)



def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
