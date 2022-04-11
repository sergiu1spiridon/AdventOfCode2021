import atexit
import time

def get_lesser_risk_path_p1(filename):
    lines = open(filename).readlines()

    matrix = []
    matrix_for_pd = []

    for line in lines:
        matrix.append(list(map(int, list(line.rstrip('\n')))))
        matrix_for_pd.append([0] * len(line.rstrip('\n')))

    matrix_big = []
    matrix_for_pd_2 = []

    for i in range(5 * len(matrix)):
        matrix_big.append([0] * 5 * len(matrix[0]))
        matrix_for_pd_2.append([0] * 5 * len(matrix[0]))
        for j in range(5 * len(matrix[0])):
            a = (matrix[i % len(matrix)][j % len(matrix[0])]
                 + int(i / len(matrix))
                 + int(j / len(matrix[0])))
            matrix_big[i][j] = a if a < 10 else a % 10 + 1

    # remove for part 1
    matrix = matrix_big
    matrix_for_pd = matrix_for_pd_2

    n = len(matrix)
    m = len(matrix[0])

    res = 0
    last_res = 1

    while res != last_res:
        last_res = res
        for i in range(n):
            for j in range(m):
                if i + j == 0:
                    matrix_for_pd[i][j] = 0
                else:
                    if i == 0:
                        matrix_for_pd[i][j] = matrix_for_pd[i][j - 1] + matrix[i][j]
                    elif j == 0:
                        matrix_for_pd[i][j] = matrix_for_pd[i - 1][j] + matrix[i][j]
                    else:
                        matrix_for_pd[i][j] = min(matrix_for_pd[i - 1][j], matrix_for_pd[i][j - 1]) + matrix[i][j]

                        if i + 1 < n and matrix_for_pd[i + 1][j] != 0:
                            matrix_for_pd[i][j] = min(matrix_for_pd[i][j], matrix_for_pd[i + 1][j] + matrix[i][j])
                        if j + 1 < m and matrix_for_pd[i][j + 1] != 0:
                            matrix_for_pd[i][j] = min(matrix_for_pd[i][j], matrix_for_pd[i][j + 1] + matrix[i][j])
        res = matrix_for_pd[len(matrix) - 1][len(matrix[0]) - 1]

    return matrix_for_pd[len(matrix) - 1][len(matrix[0]) - 1]


if __name__ == '__main__':
    start_time = time.time()
    print(get_lesser_risk_path_p1("input"))
    print(time.time() - start_time)
