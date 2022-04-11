import queue
import re


def get_lanternfish_evolution(filename):
    initial_state = list(map(int, re.split(",", (open(filename).readlines()[0].replace("Initial state: ", "")))))

    number_of_lanternfish = 0
    number_of_days = 81

    for element in initial_state:
        dp_six = [0] * number_of_days
        dp_eight = [0] * number_of_days

        dp_six[element + 1] = 1
        dp_eight[element + 1] = 1

        number_of_lanternfish += 2

        for i in range(element + 1, number_of_days):
            if dp_six[i - 7] != 0:
                dp_six[i] += dp_six[i - 7]
                dp_eight[i] += dp_six[i - 7]
                number_of_lanternfish += dp_six[i - 7]
            if dp_eight[i - 9] != 0:
                dp_six[i] += dp_eight[i - 9]
                dp_eight[i] += dp_eight[i - 9]
                number_of_lanternfish += dp_eight[i - 9]

    return number_of_lanternfish


if __name__ == '__main__':
    print(get_lanternfish_evolution("input"))
