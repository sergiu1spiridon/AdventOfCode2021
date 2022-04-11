import re
from math import floor
from statistics import median


def get_best_diff(filename):
    my_array = list(map(int, re.split(",", (open(filename).readlines()[0]))))

    # part one
    to_reduce_to = median(my_array)
    suma = 0
    for i in my_array:
        n = abs(i - to_reduce_to)
        suma += n

    # part two
    to_reduce_to = floor(sum(my_array) / len(my_array))
    suma_part_two = 0
    for i in my_array:
        n = abs(i - to_reduce_to)
        suma_part_two += n * (n + 1) / 2

    return suma


if __name__ == '__main__':
    print(get_best_diff("input"))
