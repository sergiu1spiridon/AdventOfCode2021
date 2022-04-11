def read_integers(filename):
    with open(filename) as f:
        return [int(x) for x in f]


def see_depth_variation() -> int:
    inputs = read_integers("input")
    prev = 0

    for i in range(0, 3, 1):
        prev += inputs[i]
    print(prev)
    number_of_increases = 0
    my_sum = 0
    for i in range(3, len(inputs), 1):
        my_sum = prev + inputs[i] - inputs[i - 3]
        if my_sum > prev:
            number_of_increases += 1
        prev = my_sum

    return number_of_increases


if __name__ == '__main__':
    print(see_depth_variation())
