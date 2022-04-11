def get_bingo(filename):
    file = open(filename).readlines()

    winning_numbers = list(map(lambda x: int(x), file[0].split(",")))
    dictionary_of_winning_values = {}

    for i in range(0, len(winning_numbers)):
        dictionary_of_winning_values[winning_numbers[i]] = i

    matrices = []
    when_matrices_give_bingo = []
    new_mat = []
    for i in range(2, len(file) + 1):
        if i == len(file) or file[i] == "\n":
            smallest_bingo = 100000

            for l in range(5):
                oldest_val = 0
                oldest_val_col = 0
                # for lines
                for k in range(5):
                    if new_mat[l][k] not in dictionary_of_winning_values:
                        oldest_val = None
                        break
                    else:
                        if dictionary_of_winning_values.get(new_mat[l][k]) > oldest_val:
                            oldest_val = dictionary_of_winning_values.get(new_mat[l][k])
                if oldest_val is not None and oldest_val < smallest_bingo:
                    smallest_bingo = oldest_val

                # for column
                for k in range(5):
                    if new_mat[k][l] not in dictionary_of_winning_values:
                        oldest_val_col = None
                        break
                    else:
                        if dictionary_of_winning_values.get(new_mat[k][l]) > oldest_val_col:
                            oldest_val_col = dictionary_of_winning_values.get(new_mat[k][l])
                if oldest_val_col is not None and oldest_val_col < smallest_bingo:
                    smallest_bingo = oldest_val_col

            when_matrices_give_bingo.append(smallest_bingo)

            matrices.append(new_mat)
            new_mat = []
        else:
            new_mat.append(list(map(int, filter(lambda x: x != '' and x != '\n', file[i].split(" ")))))

    fastest_bingo = max(when_matrices_give_bingo)

    suma = 0
    for i in range(len(when_matrices_give_bingo)):
        if when_matrices_give_bingo[i] == fastest_bingo:
            print(matrices[i])
            for j in range(len(matrices[i])):
                for k in matrices[i][j]:
                    if not (k in dictionary_of_winning_values and
                            dictionary_of_winning_values[k] <= fastest_bingo):
                        suma += k
            break

    print("suma: " + str(suma) + " winning numbers: " + str(winning_numbers[fastest_bingo]))

    return suma * winning_numbers[fastest_bingo]


if __name__ == '__main__':
    print(get_bingo("input"))
