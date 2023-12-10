def main():
    lines = readLines("input.txt")
    hands = []
    for line in lines:
        split = line.split(" ")
        hands.append(Hand(split[0], int(split[1])))

    hands.sort()

    acc = 0
    for i, h in enumerate(hands):
        acc += (i + 1) * h.bid

    print(acc)

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.transformed = cards.replace("T", "B").replace("J", "1").replace("Q", "D").replace("K", "E").replace("A", "F")
        self.bid = bid
        hist = histo(cards)
        for h in hist:
            if h[0] == "J" and len(hist) != 1 :
                cnt = h[1]
                hist.remove(h)
                hist[0][1] += cnt

        if len(hist) == 1:
            # Five of kind
            self.type = 50
        elif len(hist) == 2 and hist[0][1] == 4:
            # Four of a kind
            self.type = 40
        elif len(hist) == 2 and hist[0][1] == 3:
            # Full house
            self.type = 35
        elif hist[0][1] == 3:
            # Three of a kind
            self.type = 30
        elif len(hist) == 3 and hist[0][1] == 2 and hist[1][1] == 2:
            # Two pair
            self.type = 25
        elif len(hist) == 4 and hist[0][1] == 2:
            # Pair
            self.type = 20
        else:
            # High card
            self.type = 10

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
        else:
            return self.transformed < other.transformed
def histo(list):
    acc = []
    for item in list:
        curr = None
        for a in acc:
            if a[0] == item:
                curr = a
                break
        if curr is None:
            acc.append([item, 1])
        else:
            curr[1] += 1

    acc.sort(reverse=True, key=lambda e: e[1])

    return acc

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
