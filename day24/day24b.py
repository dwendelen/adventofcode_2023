import math


def main():
    lines = readLines("input.txt")

    # 19118032354423 is too low

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

    p_x0 = hails[0][0][0]
    p_y0 = hails[0][0][1]
    p_z0 = hails[0][0][2]
    v_x0 = hails[0][1][0]
    v_y0 = hails[0][1][1]
    v_z0 = hails[0][1][2]
    p_x1 = hails[1][0][0]
    p_y1 = hails[1][0][1]
    p_z1 = hails[1][0][2]
    v_x1 = hails[1][1][0]
    v_y1 = hails[1][1][1]
    v_z1 = hails[1][1][2]


    for v_xs, v_ys in allCombinations():
        divider = (v_x0 - v_xs)*(v_y1 - v_ys) - (v_x1 - v_xs)*(v_y0 - v_ys)

        if divider != 0:
            numerator0 = (p_y0 - p_y1) * (v_x1 - v_xs) - (v_y1 - v_ys) * (p_x0 - p_x1)
            numerator1 = (p_y0 - p_y1) * (v_x0 - v_xs) - (p_x0 - p_x1) * (v_y0 - v_ys)
            m0 = numerator0 % divider
            m1 = numerator1 % divider
            if m0 == 0 and m1 == 0:
                t0 = numerator0 // divider
                t1 = numerator1 // divider
                x0 = p_x0 + v_x0 * t0
                y0 = p_y0 + v_y0 * t0
                z0 = p_z0 + v_z0 * t0
                z1 = p_z1 + v_z1 * t1
                p_xs = x0 - v_xs * t0
                p_ys = y0 - v_ys * t0

                divisor2 = (t1 - t0)
                numerator2 = (z0 * t1 - z1 * t0)
                m2 = numerator2 % divisor2

                if m2 == 0 and t0 > 0 and t1 > 0:
                    p_zs = numerator2 // divisor2
                    v_zs = (z1 - z0) // divisor2

                    ok = True
                    for hail in hails:
                        p_x = hail[0][0]
                        p_y = hail[0][1]
                        p_z = hail[0][2]
                        v_x = hail[1][0]
                        v_y = hail[1][1]
                        v_z = hail[1][2]
                        divisor3 = v_xs - v_x
                        divisor4 = v_ys - v_y
                        divisor5 = v_zs - v_z
                        if divisor3 != 0:
                            t = (p_x - p_xs) / divisor3
                        elif divisor4 != 0:
                            t = (p_y - p_ys) / divisor4
                        elif divisor5 != 0:
                            t = (p_z - p_zs) / divisor5
                        else:
                            raise "Error, no idea"
                        if t < 0:
                            ok = False
                            break
                        x = p_x + v_x * t
                        y = p_y + v_y * t
                        z = p_z + v_z * t
                        xs = p_xs + v_xs * t
                        ys = p_ys + v_ys * t
                        zs = p_zs + v_zs * t
                        if x != xs or y != ys or z != zs:
                            ok = False
                            break
                    if ok:
                        print(p_xs)
                        print(p_ys)
                        print(p_zs)
                        print(p_xs + p_ys + p_zs)
                        return




    # x0 = p_x0 + v_x0 * t0
    # y0 = p_y0 + v_y0 * t0
    # z0 = p_z0 + v_z0 * t0
    # x0 = p_xs + v_xs * t0
    # y0 = p_ys + v_ys * t0
    # z0 = p_zs + v_zs * t0

    # p_x0 + v_x0 * t0 = p_xs + v_xs * t0
    # p_y0 + v_y0 * t0 = p_ys + v_ys * t0
    # p_x1 + v_x1 * t1 = p_xs + v_xs * t1
    # p_y1 + v_y1 * t1 = p_ys + v_ys * t1

    # p_xs = p_x0 + v_x0 * t0 - v_xs * t0
    # p_xs = (v_x0 - v_xs) * t0 + p_x0
    # p_xs = (v_x1 - v_xs) * t1 + p_x1

    # (v_x0 - v_xs) * t0 + p_x0 = (v_x1 - v_xs) * t1 + p_x1
    # (v_x0 - v_xs) * t0 + p_x0 - p_x1 = t1
    # --------------------------------
    #          (v_x1 - v_xs)
    #
    # (v_y0 - v_ys) * t0 + p_y0 - p_y1 = t1
    # --------------------------------
    #          (v_y1 - v_ys)
    #
    # (v_x0 - v_xs) * t0 + p_x0 - p_x1   (v_y0 - v_ys) * t0 + p_y0 - p_y1
    # -------------------------------- = --------------------------------
    #          (v_x1 - v_xs)                (v_y1 - v_ys)
    #
    # (v_x0 - v_xs)(v_y1 - v_ys) * t0 + (p_x0 - p_x1)(v_y1 - v_ys) = (v_x1 - v_xs)(v_y0 - v_ys) * t0 + (p_y0 - p_y1)(v_x1 - v_xs)
    # ((v_x0 - v_xs)(v_y1 - v_ys) - (v_x1 - v_xs)(v_y0 - v_ys) ) * t0 = (p_y0 - p_y1)(v_x1 - v_xs) - (p_x0 - p_x1)(v_y1 - v_ys)
    #
    #       (p_y0 - p_y1)(v_x1 - v_xs) - (p_x0 - p_x1)(v_y1 - v_ys)
    # t0 = --------------------------------------------------------
    #       (v_x0 - v_xs)(v_y1 - v_ys) - (v_x1 - v_xs)(v_y0 - v_ys)
    #
    # ---
    # (v_x0 - v_xs)(v_y1 - v_ys) - (v_x1 - v_xs)(v_y0 - v_ys)           (p_y0 - p_y1)(v_x1 - v_xs) - (v_y1 - v_ys)(p_x0 - p_x1)
    # -------------------------------------------------------  t0    =  -------------------------------------------------------
    #           (v_x1 - v_xs)(v_y1 - v_ys)                              (v_y1 - v_ys)     (v_x1 - v_xs)
    #
    #
    #         (p_y0 - p_y1)(v_x1 - v_xs)(v_x1 - v_xs)(v_y1 - v_ys) - (v_y1 - v_ys)(p_x0 - p_x1)(v_x1 - v_xs)(v_y1 - v_ys)
    #   t0 = -------------------------------------------------------------------------------------------------------------
    #         (v_y1 - v_ys)(v_x1 - v_xs)(v_x0 - v_xs)(v_y1 - v_ys) - (v_y1 - v_ys)(v_x1 - v_xs)(v_x1 - v_xs)(v_y0 - v_ys)
    #
    #         (p_y0 - p_y1)(v_x1 - v_xs) - (p_x0 - p_x1)(v_y1 - v_ys)
    #   t0 = ---------------------------------------------------------
    #         (v_x0 - v_xs)(v_y1 - v_ys) - (v_x1 - v_xs)(v_y0 - v_ys)
    #
    #         (p_y1 - p_y0)(v_x0 - v_xs) - (v_y0 - v_ys)(p_x1 - p_x0)
    #   t1 = ---------------------------------------------------------
    #         (v_x1 - v_xs)(v_y0 - v_ys) - (v_x0 - v_xs)(v_y1 - v_ys)
    #
    #         (p_y0 - p_y1)(v_x0 - v_xs) - (p_x0 - p_x1)(v_y0 - v_ys)
    #   t1 = ---------------------------------------------------------
    #         (v_x0 - v_xs)(v_y1 - v_ys) - (v_x1 - v_xs)(v_y0 - v_ys)
    #
    #  =============================
    #
    #   z0 = p_zs + v_zs * t0
    #   z1 = p_zs + v_zs * t1

    #   z0 * t1 = p_zs * t1 + v_zs * t0 * t1
    #   z1 * t0 = p_zs * t0 + v_zs * t1 * t0
    #   z0 * t1 - z1 * t0 = (t1 - t0) p_zs
    #   p_zs = (z0 * t1 - z1 * t0) / (t1 - t0)

    #  z0 - z1 = v_zs (t0 - t1)
    #  v_zs = (z0 - z1)/(t0 - t1)
    #
    #  ============
    #  x = p_x + t * v_x
    #  x = p_xs + t * v_xs
    #  p_x + t * v_x = p_xs + t * v_xs
    #  t = (p_x - p_xs) / (v_xs - v_x)

def allCombinations():
    d = 0
    while True:
        for i in range(-d, d):
            # top
            yield (i, d)
            # right
            yield (d, -i)
            # bottom
            yield (-i, -d)
            # left
            yield (-d, i)
        d += 1
def readLines(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines

main()
