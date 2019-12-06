# directions: 0 up, 1 right, 2 down, 3 left


def main():
    f = open("input/3_1.txt")
    i1 = f.readline()
    i2 = f.readline()

    d1 = read_directions(i1)
    d2 = read_directions(i2)

    path = {}
    cx = 0
    cy = 0

    for d, x in d1:
        if d == 0:
            for i in range(cy + 1, cy + x + 1):
                path[(cx, i)] = True
            cy += x
        elif d == 1:
            for i in range(cx + 1, cx + x + 1):
                path[(i, cy)] = True
            cx += x
        elif d == 2:
            for i in range(cy - 1, cy - x - 1):
                path[(cx, i)] = True
            cy -= x
        elif d == 3:
            for i in range(cx - 1, cx - x - 1):
                path[(i, cy)] = True
            cx -= x

    cx = 0
    cy = 0
    intersections = []
    for d, x in d2:
        if d == 0:
            for i in range(cy + 1, cy + x + 1):
                if (cx, i) in path:
                    intersections.append((cx, i))
            cy += x
        elif d == 1:
            for i in range(cx + 1, cx + x + 1):
                if (i, cy) in path:
                    intersections.append((i, cy))
            cx += x
        elif d == 2:
            for i in range(cy - 1, cy - x - 1):
                if (cx, i) in path:
                    intersections.append((cx, i))
            cy -= x
        elif d == 3:
            for i in range(cx - 1, cx - x - 1):
                if (i, cy) in path:
                    intersections.append((i, cy))
            cx -= x

    print(min(intersections, key=lambda p: abs(p[0]) + abs(p[1])))




def read_directions(s):
    raw = s.split(",")
    output = []
    for bit in raw:
        dir_s = bit[0]
        if dir_s == 'U':
            direction = 0
        elif dir_s == 'R':
            direction = 1
        elif dir_s == 'D':
            direction = 2
        else:
            direction = 3
        distance_s = bit[1:]
        output.append((direction, int(distance_s)))
    return output


if __name__ == '__main__':
    main()
