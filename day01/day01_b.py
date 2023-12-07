f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

keywords = [
    ["1", 1], ["one", 1],
    ["2", 2], ["two", 2],
    ["3", 3], ["three", 3],
    ["4", 4], ["four", 4],
    ["5", 5], ["five", 5],
    ["6", 6], ["six", 6],
    ["7", 7], ["seven", 7],
    ["8", 8], ["eight", 8],
    ["9", 9], ["nine", 9]
]

def perLine(line):
    first = 9999999
    last = -1
    firstVal = -1
    lastVal = -1
    for keyword in keywords:
        myFirst = line.find(keyword[0])
        if myFirst != -1 and myFirst < first:
            first = myFirst
            firstVal = keyword[1]

        myLast = line.rfind(keyword[0])
        if myLast != -1 and myLast > last:
            last = myLast
            lastVal = keyword[1]


    return 10 * firstVal + lastVal

bla = sum(map(perLine, lines))

print(bla)