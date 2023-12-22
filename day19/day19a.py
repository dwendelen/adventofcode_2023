def main():
    lines = readLines("input.txt")
    split = split_list(lines, "")
    instructionLines = split[0]
    itemLines = split[1]

    workflows = {}

    for line in instructionLines:
        idxO = line.index("{")
        idxC = line.index("}")
        name = line[:idxO]
        pieces = line[idxO + 1: idxC].split(",")
        acc = []
        for piece in pieces[:len(pieces) - 1]:
            idx = piece.index(":")
            var = piece[0]
            cmp = piece[1]
            val = int(piece[2:idx])
            tgt = piece[idx + 1:]
            def predicate(e, var = var, cmp = cmp, val = val):
                if var in e:
                    if cmp == "<":
                        return e[var] < val
                    else:
                        return e[var] > val
                else:
                    return False
            acc.append((predicate, tgt))
        acc.append((lambda e: True, pieces[len(pieces) - 1]))
        workflows[name] = acc

    acc = 0
    for line in itemLines:
        props = line[1:len(line) - 1].split(",")
        item = {}
        for prop in props:
            item[prop[0]] = int(prop[2:])

        curr = workflows["in"]
        run = True
        while run:
            for pred, wf in curr:
                if pred(item):
                    if wf == "A":
                        acc += item["x"]
                        acc += item["m"]
                        acc += item["a"]
                        acc += item["s"]
                        run = False
                        break
                    elif wf == "R":
                        run = False
                        break
                    else:
                        curr = workflows[wf]
                        break

    print(acc)

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

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()