def main():
    lines = readLines("input.txt")
    split = split_list(lines, "")
    instructionLines = split[0]

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
            acc.append(Instruction(var, cmp, val, tgt))

        acc.append(Instruction("x", "F", 0, pieces[len(pieces) - 1]))
        workflows[name] = acc

    acc = apply(workflows, "in", {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)})
    print(acc)

def apply(workflows, wfName, item):
    if wfName == "R":
        return 0
    elif wfName == "A":
        return (item["x"][1] - item["x"][0]) * (item["m"][1] - item["m"][0]) * (item["a"][1] - item["a"][0]) * (item["s"][1] - item["s"][0])

    wf = workflows[wfName]
    acc = 0
    for step in wf:
        if step.cmp == "F":
            acc += apply(workflows, step.target, item)
        elif step.cmp == "<":
            mn = item[step.key][0]
            mx = item[step.key][1]
            newItem1 = item.copy()
            newItem1[step.key] = (min(mn, step.val), min(mx, step.val))
            acc += apply(workflows, step.target, newItem1)
            newItem2 = item.copy()
            newItem2[step.key] = (max(mn, step.val), max(mx, step.val))
            item = newItem2
        elif step.cmp == ">":
            mn = item[step.key][0]
            mx = item[step.key][1]
            newItem1 = item.copy()
            newItem1[step.key] = (max(mn, step.val + 1), max(mx, step.val + 1))
            acc += apply(workflows, step.target, newItem1)
            newItem2 = item.copy()
            newItem2[step.key] = (min(mn, step.val + 1), min(mx, step.val + 1))
            item = newItem2
    return acc
class Instruction:
    def __init__(self, key, cmp, val, target):
        self.key = key
        self.cmp = cmp
        self.val = val
        self.target = target

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