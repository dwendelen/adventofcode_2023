def main():
    lines = readLines("input.txt")

    acc = 0
    for line in lines:
        split = line.split(" ")
        groups = list(map(int, split[1].split(",")))
        sln = tryCombo(split[0], groups)
        print(sln)
        acc += sln

    print(acc)

def tryCombo(line: str, groups):
    idx = line.find("?")
    if idx == -1:
        cnt = 0
        myGroup = []
        for i in line:
            if i == "#":
                cnt += 1
            else:
                if cnt != 0:
                    myGroup.append(cnt)
                    cnt = 0
        if cnt != 0:
            myGroup.append(cnt)
        if myGroup == groups:
            return 1
        else:
            return 0
    else:
        combo1 = tryCombo(line[:idx] + "." + line[idx + 1:], groups)
        combo2 = tryCombo(line[:idx] + "#" + line[idx + 1:], groups)
        return combo1 + combo2
def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
