import re


def get_folding_points_p1(filename):
    lines = open(filename).readlines()
    dictionary_for_matrix = []
    split_by = []

    n = 0
    m = 0

    for line in lines:
        split_line = line.rstrip('\n').split(",")
        if len(split_line) == 2:
            dictionary_for_matrix.append((int(split_line[1]), int(split_line[0])))
            m = max(n, int(split_line[1]))
            n = max(m, int(split_line[0]))
        if len(split_line) == 1 and "" not in split_line:
            temp_arr = re.split("along |=", line.rstrip('\n'))
            split_by.append((temp_arr[1], int(temp_arr[2])))

    # print(len(dictionary_for_matrix))
    n += 1
    m += 1
    print(n, m)
    total = 0
    for i in range(len(split_by)):
        y = 0
        x = 0
        if split_by[i][0] == 'y':
            y = split_by[i][1]
        if split_by[i][0] == 'x':
            x = split_by[i][1]

        if y != 0:
            for row in range(1, n - y):
                for col in range(m):
                    if dictionary_for_matrix.__contains__((y + row, col)):
                        if not dictionary_for_matrix.__contains__((y - row, col)):
                            dictionary_for_matrix.append((y - row, col))
                        dictionary_for_matrix.remove((y + row, col))
            n = n - y

        if x != 0:
            print(x)
            for row in range(n):
                for col in range(0, m - x):
                    if dictionary_for_matrix.__contains__((row, x + col)):
                        if not dictionary_for_matrix.__contains__((row, x - col)):
                            dictionary_for_matrix.append((row, x - col))
                        dictionary_for_matrix.remove((row, x + col))
            m = m - x

    for row in range(n):
        arr = []
        for col in range(m):
            arr.append('#' if dictionary_for_matrix.__contains__((row, col)) else '.')
        print(arr)

    print(dictionary_for_matrix)

    return len(dictionary_for_matrix)


if __name__ == '__main__':
    print(get_folding_points_p1("input"))
