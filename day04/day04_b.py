import re

def main():
    lines = readLines("input.txt")
    cards = []
    for line in lines:
        card = parseCard(line)
        calcMatch(card)
        cards.append(card)

    acc = 0
    for i, card in enumerate(cards):
        calcCards(i, cards)
        acc += card.cards

    print(acc)

def calcMatch(card):
    matches = 0
    for w in card.winning:
        for m in card.mine:
            if w == m:
                matches += 1
    card.matches = matches

def calcCards(i, cards):
    card = cards[i]
    if card.cards != 0:
        return
    else:
        acc = 1
        for j in range(card.matches):
            calcCards(j + i + 1, cards)
            acc += cards[j + i + 1].cards

        card.cards = acc

def parseCard(line):
    cardId = int(line[5:line.index(": ")])
    content = line[line.index(": ") + 2:]
    parts = content.split("|")

    win = list(filter(lambda p: p != "", map(lambda p: p.strip(), parts[0].split(" "))))
    mine = list(filter(lambda p: p != "", map(lambda p: p.strip(), parts[1].split(" "))))

    card = Card()
    card.winning = win
    card.mine = mine

    return card

class Card:
    winning = []
    mine = []
    matches = 0
    cards = 0


def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
