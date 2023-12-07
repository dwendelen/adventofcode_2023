f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

def perLine(line):
    fltr = list(filter(lambda l: l.isnumeric(), list(line)))
    return int(fltr[0] + fltr[-1])

bla = sum(map(perLine, lines))

print(bla)