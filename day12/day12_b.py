cache = {}

def main():
    lines = readLines("input.txt")

    lineNb = 1

    acc = 0
    for line in lines:
        split = line.split(" ")
        wordPart = split[0]
        groupPart = split[1]

        for i in range(4):
            wordPart = wordPart + "?" + split[0]
            groupPart = groupPart + "," + split[1]

        groups = tuple(map(int, groupPart.split(",")))

        wordGroups = parse(wordPart)

        solved = solve(wordGroups, groups)
        print(str(lineNb) + ": " + str(solved))
        acc += solved
        lineNb += 1

    print("-------------")
    print(acc)

def parse(text):
    acc1 = []
    acc2 = []
    acc3 = 0

    for c in text:
        if c == ".":
            if len(acc2) != 0:
                acc2.append(acc3)
                acc3 = 0
                acc1.append(tuple(acc2,))
                acc2 = []
            else:
                if acc3 != 0:
                    acc1.append((acc3,))
                    acc3 = 0
        elif c == "?":
            acc2.append(acc3)
            acc3 = 0
        elif c == "#":
            acc3 += 1
        else:
            raise "Error"
    if len(acc2) != 0:
        acc2.append(acc3)
        acc1.append(tuple(acc2))
    else:
        if acc3 != 0:
            acc1.append((acc3,))
    return tuple(acc1)

def solve(wordGroups, groups):
    def onCombi(combi, acc1):
        acc2 = 1
        for wg, g in combi:
            acc2 *= solveWordGroupCached(wg, g)
        return acc1 + acc2

    return findCombinations(wordGroups, groups, (), onCombi, 0)


def findCombinations(workGroups, groups, acc, onCombination, accCombi):
    if len(workGroups) == 0:
        if len(groups) == 0:
            accCombi = onCombination(acc, accCombi)
            return accCombi
        else:
            return accCombi
    else:
        wg = workGroups[0]
        tail = workGroups[1:]
        wgMin = 0
        wgMax = -1
        for i in wg:
            wgMax += i + 1
            wgMin += i
        if wgMin == 0:
            accCombi = findCombinations(tail, groups, acc + ((wg, ()),), onCombination, accCombi)
        gLen = -1
        for i, g in enumerate(groups):
            gLen += g + 1
            if wgMin <= gLen <= wgMax:
                accCombi = findCombinations(tail, groups[i + 1:], acc + ((wg, groups[:i + 1]),), onCombination, accCombi)
        return accCombi

def solveWordGroupCached(wordGroup, groups):
    key = (wordGroup, groups)
    if key in cache:
        return cache[key]
    else:
        sln = solveWordGroup(wordGroup, groups)
        cache[key] = sln
        return sln

def solveWordGroup(wordGroup, groups):
    if len(groups) == 0:
        # [...] []
        if len(wordGroup) == 0:
            # []  []
            return 1
        else:
            # [wg, ...] []
            wg = wordGroup[0]
            if wg == 0:
                return solveWordGroupCached(wordGroup[1:], groups)
            else:
                return 0
    else:
        # [...] [grp, ...]
        if len(wordGroup) == 0:
            return 0
        else:
            # [wg, ...] [grp, ...]
            wg = wordGroup[0]
            if wg == 0:
                # [0, ...] [grp, ...]
                #  ==
                # [...] [...]
                # [...] [grp, ...]
                res1 = eatGroup(wordGroup, groups[0], groups[1:])
                res2 = solveWordGroupCached(wordGroup[1:], groups)
                return res1 + res2
            else:
                return eatGroup(wordGroup, groups[0], groups[1:])

def eatGroup(wordGroup, grp, tail):
    if grp == 0:
        # [...] 0
        if len(wordGroup) == 0:
            return 0
        else:
            wg = wordGroup[0]
            if wg == 0:
                # [0, ...] 0
                return solveWordGroupCached(wordGroup[1:], tail)
            else:
                return 0
    else:
        if len(wordGroup) == 0:
            # [] 3
            return 0
        else:
            # [wg, ...] 3
            wg = wordGroup[0]
            if grp < wg:
                # [4, ...] 3
                return 0
            elif grp == wg:
                # [4, ...] 4
                return solveWordGroupCached(wordGroup[1:], tail)
            else:
                # [3, ...] 5
                # [0, ...] 2
                # [...]    1
                return eatGroup(wordGroup[1:], grp - wg - 1, tail)

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
