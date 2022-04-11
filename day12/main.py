def DFS(paths, visited, curr, twice_visited_one):
    if curr == "end":
        if twice_visited_one != "":
            if twice_visited_one not in visited:
                return 0
        return 1

    s = 0
    for neighbor in paths[curr]:
        if neighbor not in visited:
            if not neighbor.isupper():
                visited.append(neighbor)
                s += DFS(paths, visited, neighbor, twice_visited_one)
                visited.remove(neighbor)
                if twice_visited_one == "" and neighbor != "start" and neighbor != "end":
                    s += DFS(paths, visited, neighbor, neighbor)
            else:
                s += DFS(paths, visited, neighbor, twice_visited_one)

    return s


def get_number_of_paths_p1(filename):
    lines = open(filename).readlines()

    paths = {}

    for line in lines:
        dic = line.rstrip('\n').split("-")

        if dic[0] not in paths:
            paths[dic[0]] = []
        if dic[1] not in paths:
            paths[dic[1]] = []
        paths[dic[0]].append(dic[1])
        paths[dic[1]].append(dic[0])

    visited = ["start"]

    return DFS(paths, visited, "start", "")


if __name__ == '__main__':
    print(get_number_of_paths_p1("input"))
