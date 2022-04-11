from array import array


def read_from_file(filename):
    with open(filename) as f:
        return [x for x in f]


def get_generator_rating(my_input, type_of_search):
    vector_of_sums = [0 for i in range(len(my_input[0]) - 1)]
    one_array = []
    zero_array = []
    n = len(my_input[0]) - 1

    for i in range(0, n):
        if len(my_input) == 1:
            break
        for x in my_input:
            if x[i] == '1':
                vector_of_sums[i] += 1
                one_array.append(x)
            else:
                vector_of_sums[i] -= 1
                zero_array.append(x)

        if vector_of_sums[i] == 0:
            if type_of_search == 1:
                my_input = list(one_array)
            else:
                my_input = list(zero_array)
        elif vector_of_sums[i] * type_of_search > 0:
            my_input = list(one_array)
        else:
            my_input = list(zero_array)
        one_array = []
        zero_array = []

    return my_input


def get_diagnostic_report():
    my_input = read_from_file("input")
    my_input2 = list(my_input)

    gama = int(get_generator_rating(my_input, 1)[0], 2)
    epsilon = int(get_generator_rating(my_input2, -1)[0], 2)

    return gama * epsilon


if __name__ == '__main__':
    print(get_diagnostic_report())
