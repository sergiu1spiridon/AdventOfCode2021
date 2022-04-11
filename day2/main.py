def read_pairs_from_file(filename):
    with open(filename) as f:
        return [(x.split()[0], int(x.split()[1])) for x in f]


def get_course() -> int:
    dictionary = {
        "forward": (0, 1),
        "up": (1, -1),
        "down": (1, 1)
    }
    myInputs = read_pairs_from_file("input")
    depth = 0
    horizontal_position = 0
    aim = 0

    for i in myInputs:
        couple = dictionary[i[0]]
        if couple[0] == 0:
            horizontal_position += couple[1] * i[1]
            depth += aim * i[1]
        elif couple[0] == 1:
            aim += couple[1] * i[1]

    return horizontal_position * depth


if __name__ == '__main__':
    print(get_course())
