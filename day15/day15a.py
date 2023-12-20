def main():
    lines = readLines("input.txt")
    codes = lines[0].split(",")

    acc = 0
    for code in codes:
        hash = 0
        for char in code:
            hash = ((hash + ord(char)) * 17) & 255
        acc += hash

    print(acc)
def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
