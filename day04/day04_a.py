import re

def main():
    res = foldLines("input.txt", 0, action)
    print(res)

def action(acc, line):
    game = parseCard(line)
    matches = 0
    for w in game["winning"]:
        for m in game["mine"]:
            if w == m:
                matches += 1
    if matches == 0:
        return acc
    else:
        return acc + (1 << (matches - 1))

def parseCard(line):
    cardId = int(line[5:line.index(": ")])
    content = line[line.index(": ") + 2:]
    parts = content.split("|")

    win = list(filter(lambda p: p != "", map(lambda p: p.strip(), parts[0].split(" "))))
    mine = list(filter(lambda p: p != "", map(lambda p: p.strip(), parts[1].split(" "))))


    return {
        "id": cardId,
        "winning": win,
        "mine": mine
    }

def foldLines(path, init, fn):
    state = init
    f = open(path, "r")
    lines = f.read().splitlines()
    for l in lines:
        state = fn(state, l)
    f.close()
    return state

main()
