def main():
    f = open("input/2_1.txt")
    p = list(map(int, f.read().split(",")))

    for i in range(100):
        for j in range(100):
            if execute(p.copy(), i, j) == 19690720:
                print(100 * i + j)
                break


def execute(p, a, b):

    p[1] = a
    p[2] = b

    i = 0
    while True:
        code = p[i]
        if code == 99:
            break
        else:
            a1 = p[i + 1]
            a2 = p[i + 2]
            a3 = p[i + 3]
            if code == 1:
                p[a3] = p[a1] + p[a2]
            elif code == 2:
                p[a3] = p[a1] * p[a2]
            else:
                return 0
            i += 4
    return p[0]

if __name__ == '__main__':
    main()