import re

def main():
    res = foldLines("input.txt", 0, action)
    print(res)

def action(acc, line):
    game = parseGame(line)
    for d in game['draws']:
        if d.get("red", 0) > 12 or d.get("green", 0) > 13 or d.get("blue", 0) > 14:
            return acc
    return acc + game["id"]

def parseGame(line):
    gameId = int(line[5:line.index(": ")])
    drawLines = line[line.index(": ") + 2:].split("; ")
    draws = []
    for drawLine in drawLines:
        items = {}
        for itemLine in drawLine.split(", "):
            pieces = itemLine.split(" ")
            items[pieces[1]] = int(pieces[0])
        draws.append(items)

    return {
        "id": gameId,
        "draws": draws
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
