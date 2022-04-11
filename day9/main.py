def smoke_basin_p1(filename):
    matrix = []
    f = open(filename, "r")
    for line in f.readlines():
        matrix.append(list(map(int, line.strip())))
    final_sum = 0

    dir_i = [-1, 0, 1, 0]
    dir_j = [0, -1, 0, 1]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            is_local_min = True
            for k in range(4):
                if 0 <= i + dir_i[k] < len(matrix) and 0 <= j + dir_j[k] < len(matrix[i]):
                    if matrix[i][j] >= matrix[i + dir_i[k]][j + dir_j[k]]:
                        is_local_min = False
                        break
            if is_local_min:
                final_sum += matrix[i][j] + 1

    return final_sum


def smoke_basin_p2(filename):
    matrix = []
    visited = []
    sizes = []
    f = open(filename, "r")
    for line in f.readlines():
        matrix.append(list(map(int, line.strip())))
        visited.append([0] * len(line.strip()))

    dir_i = [-1, 0, 1, 0]
    dir_j = [0, -1, 0, 1]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            is_local_min = True

            for k in range(4):
                if 0 <= i + dir_i[k] < len(matrix) and 0 <= j + dir_j[k] < len(matrix[i]):
                    if matrix[i][j] >= matrix[i + dir_i[k]][j + dir_j[k]]:
                        is_local_min = False
                        break
            if is_local_min:
                my_queue = [(i, j)]
                size = 0

                while len(my_queue) != 0:
                    el = my_queue.pop()
                    visited[el[0]][el[1]] = 1
                    size += 1

                    for k in range(4):
                        if 0 <= el[0] + dir_i[k] < len(matrix) and 0 <= el[1] + dir_j[k] < len(matrix[i]):
                            if matrix[el[0]][el[1]] < matrix[el[0] + dir_i[k]][el[1] + dir_j[k]]:
                                if visited[el[0] + dir_i[k]][el[1] + dir_j[k]] == 0 and matrix[el[0] + dir_i[k]][el[1] + dir_j[k]] != 9:
                                    my_queue.append((el[0] + dir_i[k], el[1] + dir_j[k]))
                                    visited[el[0] + dir_i[k]][el[1] + dir_j[k]] = 1

                sizes.append(size)

    sizes.sort(reverse=True)

    final_product = 1

    for i in range(3):
        final_product *= sizes[i]

    return final_product


if __name__ == '__main__':
    print(smoke_basin_p2("input"))
