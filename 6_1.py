def main():

    orbits = {}
    planets = []
    parent = {}

    with open("input/6_1.txt") as f:
        for line in f:
            data = line.strip().split(")")

            parent[data[1]] = data[0]

            if data[0] in orbits:
                orbits[data[0]].append(data[1])
            else:
                orbits[data[0]] = [data[1]]

            if data[0] not in planets:
                planets.append(data[0])
            if data[1] not in planets:
                planets.append(data[1])

    for planet in planets:
        if planet not in orbits:
            orbits[planet] = []
        if planet not in parent:
            parent[planet] = None

    order = dfs(planets, orbits)

    orbit_count = {}
    for planet in order:
        if parent[planet] is None:
            orbit_count[planet] = 0
        else:
            orbit_count[planet] = orbit_count[parent[planet]] + 1

    print(sum([orbit_count[planet] for planet in planets]))


def dfs_visit(planet, visited, orbits, top_sort):
    visited[planet] = True
    for child in orbits[planet]:
        if not visited[child]:
            dfs_visit(child, visited, orbits, top_sort)
    top_sort.append(planet)


def dfs(planets, orbits):
    visited = {}

    for planet in planets:
        visited[planet] = False

    top_sort = []
    for planet in planets:
        if not visited[planet]:
            dfs_visit(planet, visited, orbits, top_sort)

    return list(reversed(top_sort))


if __name__ == '__main__':
    main()
