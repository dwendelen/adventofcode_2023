def main():
    # lines = readLines("example.txt")
    # boxMin = 7
    # boxMax = 27

    lines = readLines("input.txt")
    boxMin = 200000000000000
    boxMax = 400000000000000

    hails = []

    for line in lines:
        split1 = line.split(" @ ")
        pos = split1[0].split(", ")
        vel = split1[1].split(", ")
        hail = (
            (int(pos[0]), int(pos[1]), int(pos[2])),
            (int(vel[0]), int(vel[1]), int(vel[2]))
        )
        hails.append(hail)

    # x = p_x0 + v_x0 * t0
    # y = p_y0 + v_y0 * t0
    # x = p_x1 + v_x1 * t1
    # y = p_y1 + v_y1 * t1
    #
    # Solve to:
    #
    #      v_x1(x0-y1) - v_y1(x0 - x1)
    # t0 = ---------------------------
    #         v_x0 v_y1 - v_y0 v_x1
    #
    # Similar for t1, but do divisor and numerator times minus one to get the same divider
    #

    acc = 0
    for i in range(len(hails)):
        for j in range(i + 1, len(hails)):
            hail0 = hails[i]
            hail1 = hails[j]

            x0 = hail0[0][0]
            y0 = hail0[0][1]
            v_x0 = hail0[1][0]
            v_y0 = hail0[1][1]

            x1 = hail1[0][0]
            y1 = hail1[0][1]
            v_x1 = hail1[1][0]
            v_y1 = hail1[1][1]

            divider = v_x0*v_y1 - v_y0*v_x1
            if divider != 0:
                t0 = (v_x1 * (y0 - y1) - v_y1*(x0 - x1)) / divider
                t1 = (v_x0 * (y0 - y1) - v_y0*(x0 - x1)) / divider
                x = x0 + t0 * v_x0
                y = y0 + t0 * v_y0
                x2 = x1 + t1 * v_x1
                y2 = y1 + t1 * v_y1
                if boxMin <= x <= boxMax and boxMin <= y <= boxMax and t0 >= 0 and t1 >= 0:
                    acc += 1
    print(acc)

def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
