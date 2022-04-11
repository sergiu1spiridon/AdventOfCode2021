def identify_clock_values_p1(filename):
    lines = open(filename).readlines()

    instances_of_unique_numbers = 0

    for line in lines:
        input_split_in_two = line.split("|")

        output_part = (input_split_in_two[1].split(" "))
        output_part.remove("")

        for word in output_part:
            word = word.rstrip("\n")
            if len(word) == 2 or len(word) == 3 or len(word) == 4 or len(word) == 7:
                instances_of_unique_numbers += 1

    return instances_of_unique_numbers


def identify_clock_values_p2(filename):
    lines = open(filename).readlines()
    sum_of_all_outputs = 0

    for line in lines:
        my_digits_array = [''] * 10
        search_order = [1, 4, 7, 8, 9, 3, 0, 6, 5, 2]

        input_split_in_two = line.split("|")

        input_part = (input_split_in_two[0].split(" "))
        input_part.remove("")

        output_part = (input_split_in_two[1].split(" "))
        output_part.remove("")

        for digit_for_search in search_order:
            for word in input_part:
                if \
                        digit_for_search == 1 and not len(word) == 2 or \
                        digit_for_search == 4 and not len(word) == 4 or \
                        digit_for_search == 7 and not len(word) == 3 or \
                        digit_for_search == 8 and not len(word) == 7:
                    continue

                if digit_for_search == 9 and not (
                        len(word) == 6 and 0 not in [c in word for c in my_digits_array[4]]):
                    continue
                if digit_for_search == 3 and not (
                        len(word) == 5 and 0 not in [c in word for c in my_digits_array[7]]):
                    continue
                if digit_for_search == 0 and not (
                        len(word) == 6 and 0 not in [c in word for c in my_digits_array[7]] and word !=
                        my_digits_array[9]):
                    continue
                if digit_for_search == 6 and not (
                        len(word) == 6 and word != my_digits_array[9] and word != my_digits_array[0]):
                    continue
                if digit_for_search == 5 and not (
                        len(word) == 5 and 0 not in [c in my_digits_array[6] for c in word]):
                    continue
                if digit_for_search == 2 and not (
                        len(word) == 5 and word != my_digits_array[3] and word != my_digits_array[5]):
                    continue

                my_digits_array[digit_for_search] = word

        print(my_digits_array)

        out_decimal = 0
        for word in output_part:
            word = word.rstrip("\n")
            for i in my_digits_array:
                if 0 not in [c in i for c in word] and 0 not in [c in word for c in i]:
                    out_decimal *= 10
                    out_decimal += my_digits_array.index(i)
                    break
        print(out_decimal)

        sum_of_all_outputs += out_decimal

    return sum_of_all_outputs


if __name__ == '__main__':
    print(identify_clock_values_p2("input"))
