def get_corrupted_lines_p1(filename):
    lines = open(filename).readlines()

    dictionary_of_par_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    dictionary_of_par_values = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    suma = 0

    for line in lines:
        array = [char for char in line.rstrip('\n')]

        my_stack = []

        for i in array:
            if i in dictionary_of_par_pairs.keys():
                my_stack.append(i)
            else:
                last_added_in_stack = my_stack[-1]
                del my_stack[-1]

                if dictionary_of_par_pairs.get(last_added_in_stack) != i:
                    suma += dictionary_of_par_values.get(i)
                    break

    return suma


def get_corrupted_lines_p2(filename):
    lines = open(filename).readlines()

    dictionary_of_par_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }

    dictionary_of_par_values = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    array_of_sums = []

    for line in lines:
        suma = 0
        is_valid = True

        array = [char for char in line.rstrip('\n')]

        my_stack = []

        for i in array:
            if i in dictionary_of_par_pairs.keys():
                my_stack.append(i)
            else:
                last_added_in_stack = my_stack[-1]
                del my_stack[-1]

                if dictionary_of_par_pairs.get(last_added_in_stack) != i:
                    is_valid = False
                    break
        if is_valid:
            while len(my_stack) > 0:
                suma *= 5
                suma += dictionary_of_par_values[dictionary_of_par_pairs[my_stack[-1]]]
                del my_stack[-1]
            array_of_sums.append(suma)

    array_of_sums.sort()

    return array_of_sums[int(len(array_of_sums) / 2)]


if __name__ == '__main__':
    print(get_corrupted_lines_p2("input"))
