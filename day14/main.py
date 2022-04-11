import math


def string_multiplication_p2(filename, number_of_steps):
    lines = open(filename).readlines()

    input_string = lines[0].rstrip('\n')

    dictionary_of_transitions = {}
    dictionary_letter_to_number_of_appearances = {}

    for i in input_string:
        dictionary_letter_to_number_of_appearances[i] = 0

    for i in range(2, len(lines)):
        line_split = lines[i].rstrip('\n').split(" -> ")
        dictionary_of_transitions[line_split[0]] = line_split[1]
        dictionary_letter_to_number_of_appearances[line_split[1]] = 0

    dictionary_letter_to_number_of_appearances[input_string[len(input_string) - 1]] += 1

    dictionary_pair_to_num = {}

    for i in range(0, len(input_string) - 1):
        dictionary_letter_to_number_of_appearances[input_string[i]] += 1
        if (input_string[i] + input_string[i + 1]) in dictionary_pair_to_num:
            dictionary_pair_to_num[input_string[i] + input_string[i + 1]] += 1
        else:
            dictionary_pair_to_num[input_string[i] + input_string[i + 1]] = 1

    for k in range(number_of_steps):
        new_dic = {}
        for i in dictionary_pair_to_num:
            dictionary_letter_to_number_of_appearances[dictionary_of_transitions[i]] += dictionary_pair_to_num[i]
            el1 = i[0] + dictionary_of_transitions[i]
            el2 = dictionary_of_transitions[i] + i[1]
            if el1 in new_dic:
                new_dic[el1] += dictionary_pair_to_num[i]
            else:
                new_dic[el1] = dictionary_pair_to_num[i]

            if el2 in new_dic:
                new_dic[el2] += dictionary_pair_to_num[i]
            else:
                new_dic[el2] = dictionary_pair_to_num[i]

        dictionary_pair_to_num = new_dic

    print(dictionary_letter_to_number_of_appearances)

    return max(dictionary_letter_to_number_of_appearances.values()) - min(dictionary_letter_to_number_of_appearances.values())


def string_multiplication_p1(filename, number_of_steps):
    lines = open(filename).readlines()

    input_string = lines[0].rstrip('\n')

    dictionary_of_transitions = {}
    dictionary_letter_to_number_of_appearances = {}

    for i in input_string:
        dictionary_letter_to_number_of_appearances[i] = 0

    for i in range(2, len(lines)):
        line_split = lines[i].rstrip('\n').split(" -> ")
        dictionary_of_transitions[line_split[0]] = line_split[1]
        dictionary_letter_to_number_of_appearances[line_split[1]] = 0

    dictionary_letter_to_number_of_appearances[input_string[len(input_string) - 1]] += 1
    for i in range(0, len(input_string) - 1):
        dictionary_letter_to_number_of_appearances[input_string[i]] += 1
        my_queue = [input_string[i] + input_string[i + 1]]
        steps = 1

        # print(input_string[i] + input_string[i + 1])
        while len(my_queue) > 0 and steps < pow(2, number_of_steps):
            steps += 1
            el = my_queue.pop(0)
            if el in dictionary_of_transitions:
                dictionary_letter_to_number_of_appearances[dictionary_of_transitions[el]] += 1
                el1 = el[0] + dictionary_of_transitions[el]
                el2 = dictionary_of_transitions[el] + el[1]

                my_queue.append(el1)
                my_queue.append(el2)

    maxim = 0
    minim = 0

    for k in dictionary_letter_to_number_of_appearances:
        if minim == 0:
            minim = dictionary_letter_to_number_of_appearances[k]
        minim = min(dictionary_letter_to_number_of_appearances[k], minim)
        maxim = max(dictionary_letter_to_number_of_appearances[k], maxim)

    print(dictionary_letter_to_number_of_appearances)
    return maxim - minim


if __name__ == '__main__':
    print(string_multiplication_p2("input", 40))