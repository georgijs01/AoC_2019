def main():

    orbits = {}
    # planets = []

    with open("input/6_1.txt") as f:
        for line in f:
            data = line.strip().split(")")

            if data[0] in orbits:
                orbits[data[0]].append(data[1])
            else:
                orbits[data[0]] = [data[1]]

            if data[1] in orbits:
                orbits[data[1]].append(data[0])
            else:
                orbits[data[1]] = [data[0]]

    print(dfs(orbits) - 1)


def dfs_visit(planet, visited, orbits, distance):
    visited[planet] = True
    distances = []
    for child in orbits[planet]:
        if child == 'SAN':
            return distance
        elif not visited[child]:
            distances.append(dfs_visit(child, visited, orbits, distance + 1))
    if len(distances) == 0:
        distances.append(float('inf'))
    return min(distances)


def dfs(orbits):
    visited = {}

    for planet in orbits.keys():
        visited[planet] = False

    return dfs_visit('YOU', visited, orbits, 0)


if __name__ == '__main__':
    main()
