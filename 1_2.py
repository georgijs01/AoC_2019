def main():
    f = open("input/1_1.txt")
    print(sum([calculate(int(line)) for line in f]))


def calculate(m):
    fuel = m//3-2
    if fuel <= 0:
        return 0
    else:
        return fuel + calculate(fuel)


if __name__ == '__main__':
    main()