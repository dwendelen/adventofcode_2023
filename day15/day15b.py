def main():
    lines = readLines("input.txt")
    codes = lines[0].split(",")

    boxes = []
    for _ in range(256):
        boxes.append([])

    for code in codes:
        idx = code.find("=")
        if idx == -1:
            lens = code[:len(code) - 1]

            hash = 0
            for char in lens:
                hash = ((hash + ord(char)) * 17) & 255
            box = boxes[hash]

            newBox = []
            for b in box:
                if b[0] != lens:
                    newBox.append(b)
            boxes[hash] = newBox
        else:
            lens = code[:idx]
            focal = int(code[idx + 1:])

            hash = 0
            for char in lens:
                hash = ((hash + ord(char)) * 17) & 255
            box = boxes[hash]

            found = False
            for b in box:
                if b[0] == lens:
                    b[1] = focal
                    found = True
                    break
            if not found:
                box.append([lens, focal])

    acc = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            acc += (i + 1) * (j + 1) * lens[1]

    print(acc)

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
