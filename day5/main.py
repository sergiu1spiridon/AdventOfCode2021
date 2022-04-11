import re


def get_how_many_diagonal_paths_intersect():
    file = open("input").readlines()

    matrix = {}
    count = 0

    for line in file:
        line_coordinates = list(map(int, re.split(" -> |,", line)))

        min_i = min(line_coordinates[0], line_coordinates[2])
        max_i = max(line_coordinates[0], line_coordinates[2])

        min_j = min(line_coordinates[1], line_coordinates[3])
        max_j = max(line_coordinates[1], line_coordinates[3])
        # part one
        if max_j - min_j == 0 or max_i - min_i == 0:
            for i in range(min_i, max_i + 1):
                for j in range(min_j, max_j + 1):
                    if (i, j) not in matrix:
                        matrix[(i, j)] = 0
                    elif matrix[(i, j)] == 1:
                        count += 1
                    matrix[(i, j)] += 1

        # for part two
        elif max_j - min_j == max_i - min_i:
            i_dir = -1 if line_coordinates[0] == max_i else 1
            j_dir = -1 if line_coordinates[1] == max_j else 1

            for l in range(max_j - min_j + 1):
                i = line_coordinates[0] + i_dir * l
                j = line_coordinates[1] + j_dir * l
                if (i, j) not in matrix:
                    matrix[(i, j)] = 0
                elif matrix[(i, j)] == 1:
                    count += 1
                matrix[(i, j)] += 1

    return count


if __name__ == '__main__':
    print(get_how_many_diagonal_paths_intersect())
