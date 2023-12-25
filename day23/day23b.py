def main():
    lines = readLines("input.txt")

    start = (0, 1)
    end = (len(lines) - 1, len(lines[0]) - 2)

    knownPoints = {start: Point(start), end: Point(end)}

    queue = [(start, knownPoints[start], 0, (-1, -1))]

    while len(queue) != 0:
        pos, source, dist, prev = queue.pop()
        maybeDirs = (
            (pos[0] - 1, pos[1]),
            (pos[0] + 1, pos[1]),
            (pos[0], pos[1] - 1),
            (pos[0], pos[1] + 1)
        )
        friends = []
        for newPos in maybeDirs:
            char = lines[newPos[0]][newPos[1]]
            if char != "#" and newPos != prev:
                friends.append(newPos)

        if len(friends) > 1:
            newPoint = Point(pos)
            knownPoints[pos] = newPoint
            newPoint.add(source, dist)
            source = newPoint
            dist = 0

        for friend in friends:
            if friend not in knownPoints:
                queue.append((friend, source, dist + 1, pos))
            else:
                knownPoints[friend].add(source, dist + 1)

    res = traverse(knownPoints[start], 0, [], knownPoints[end])

    print(res)

def traverse(point, dist, visited, end):
    if point == end:
        return dist
    else:
        visited.append(point)
        acc = 0
        for friend, friendsDist in point.dist.items():
            if friend not in visited:
                best = traverse(friend, dist + friendsDist, visited, end)
                if best > acc:
                    acc = best
        visited.pop()
        return acc

class Point:
    def __init__(self, pos):
        self.pos = pos
        self.dist = {}

    def add(self, point, dist):
        self.dist[point] = dist
        point.dist[self] = dist


def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines


main()
