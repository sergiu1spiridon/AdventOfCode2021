def dumbo_octo_p1(filename):
    lines = open(filename).readlines()
    matrix = []
    for l in lines:
        matrix.append([int(char) for char in l.rstrip('\n')])

    total_flashes = 0
    for step in range(100):
        flashed_this_step = list()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] += 1
                if matrix[i][j] == 10:
                    matrix[i][j] = 0
                    flashed_this_step.append((i, j))

        directions_i = [0, 0, 1, -1, 1, -1, 1, -1]
        directions_j = [1, -1, 0, 0, 1, 1, -1, -1]

        while len(flashed_this_step) > 0:
            first_in_queue = flashed_this_step.pop(0)
            x = first_in_queue[0]
            y = first_in_queue[1]
            total_flashes += 1

            for direction in range(8):
                if 0 <= x + directions_i[direction] < len(matrix) and \
                        0 <= y + directions_j[direction] < len(matrix[0]):

                    if matrix[x + directions_i[direction]][y + directions_j[direction]] != 0:
                        matrix[x + directions_i[direction]][y + directions_j[direction]] += 1

                    if matrix[x + directions_i[direction]][y + directions_j[direction]] == 10:
                        matrix[x + directions_i[direction]][y + directions_j[direction]] = 0
                        flashed_this_step.append((x + directions_i[direction], y + directions_j[direction]))

        for i in range(len(matrix)):
            print(matrix[i])
        print()

    return total_flashes

def dumbo_octo_p2(filename):
    lines = open(filename).readlines()
    matrix = []
    for l in lines:
        matrix.append([int(char) for char in l.rstrip('\n')])

    synced_step = 0
    step = 0
    while True:
        step += 1
        sync_step_was_before = True
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != 0:
                    sync_step_was_before = False

        if sync_step_was_before:
            synced_step = step - 1
            break

        flashed_this_step = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] += 1
                if matrix[i][j] == 10:
                    matrix[i][j] = 0
                    flashed_this_step.append((i, j))

        directions_i = [0, 0, 1, -1, 1, -1, 1, -1]
        directions_j = [1, -1, 0, 0, 1, 1, -1, -1]

        while len(flashed_this_step) > 0:
            first_in_queue = flashed_this_step.pop(0)
            x = first_in_queue[0]
            y = first_in_queue[1]

            for direction in range(8):
                if 0 <= x + directions_i[direction] < len(matrix) and \
                        0 <= y + directions_j[direction] < len(matrix[0]):

                    if matrix[x + directions_i[direction]][y + directions_j[direction]] != 0:
                        matrix[x + directions_i[direction]][y + directions_j[direction]] += 1

                    if matrix[x + directions_i[direction]][y + directions_j[direction]] == 10:
                        matrix[x + directions_i[direction]][y + directions_j[direction]] = 0
                        flashed_this_step.append((x + directions_i[direction], y + directions_j[direction]))

        for i in range(len(matrix)):
            print(matrix[i])
        print()

    return synced_step


if __name__ == '__main__':
    print(dumbo_octo_p2("input"))
