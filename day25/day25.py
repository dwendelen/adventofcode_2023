
def main():
    lines = readLines("input.txt")

    knownNodes = {}
    for line in lines:
        split1 = line.split(": ")
        name = split1[0]
        friendNames = split1[1].split(" ")
        if name in knownNodes:
            currentPoint = knownNodes[name]
        else:
            currentPoint = Point(name)
            knownNodes[name] = currentPoint

        for friendName in friendNames:
            if friendName in knownNodes:
                friend = knownNodes[friendName]
            else:
                friend = Point(friendName)
                knownNodes[friendName] = friend
            currentPoint.add(friend)

    # We look at loop lengths

    interestingEdges = set()

    for node in knownNodes.values():
        for friend in node.friends:
            ll = loopLength(node, friend)
            if ll > 10:
                if node.name > friend.name:
                    interestingEdges.add((node, friend))
                else:
                    interestingEdges.add((friend, node))

    # There are 3 with a loop length > 10
    # Let's try with those

    for n1, n2 in interestingEdges:
        n1.friends.remove(n2)
        n2.friends.remove(n1)

    reachable = set()
    edge = { next(iter(knownNodes.values())) }
    while len(edge) != 0:
        e = edge.pop()
        reachable.add(e)
        for friend in e.friends:
            if friend not in reachable:
                edge.add(friend)

    size1 = len(reachable)
    size2 = len(knownNodes) - size1
    res = size1 * size2
    print(res)

def loopLength(node1, node2):
    dist = 2
    visited = {node2}
    border = []
    for f in node2.friends:
        if f != node1:
            visited.add(f)
            border.append(f)
    while True:
        nextBorder = []
        while len(border) != 0:
            b = border.pop()
            if b == node1:
                return dist
            else:
                for f in b.friends:
                    if f not in visited:
                        visited.add(f)
                        nextBorder.append(f)
        border = nextBorder
        dist += 1



class Point:
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)

    def __str__(self):
        return self.name

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
