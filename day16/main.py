def get_packet_p1(i, byte_array):
    version = int(byte_array[i:i + 3], 2)
    type_id = int(byte_array[i + 3:i + 6], 2)

    i += 6
    if type_id == 4:
        packet_sum = ''

        while True:

            next_set = byte_array[i + 1:i + 5]
            packet_sum + next_set + packet_sum

            if byte_array[i] == '0':
                i += 5
                break
            i += 5

    else:
        size = 0
        temp_version_sum = 0
        if byte_array[i] == '0':
            size = int(byte_array[i + 1:i + 16], 2)
            i += 16

            while size > 0:
                a = get_packet_p1(i, byte_array)
                size -= a[0] - i
                i = a[0]
                temp_version_sum += a[1]

        elif byte_array[i] == '1':
            size = int(byte_array[i + 1:i + 12], 2)
            i += 12

            while size > 0:
                a = get_packet_p1(i, byte_array)
                size -= 1
                i = a[0]
                temp_version_sum += a[1]

        version += temp_version_sum

    # print(version)
    return i, version


def get_packet_p2(i, byte_array):
    version = int(byte_array[i:i + 3], 2)
    type_id = int(byte_array[i + 3:i + 6], 2)

    i += 6
    if type_id == 4:
        packet_sum = ''

        while True:

            next_set = byte_array[i + 1:i + 5]
            packet_sum += next_set

            if byte_array[i] == '0':
                i += 5
                break
            i += 5

        return i, int(packet_sum, 2)

    else:
        size = 0
        temp_value_sum = None
        if type_id == 0:
            temp_value_sum = 0
        elif type_id == 1:
            temp_value_sum = 1

        if byte_array[i] == '0':
            size = int(byte_array[i + 1:i + 16], 2)
            i += 16

            while size > 0:
                a = get_packet_p2(i, byte_array)
                size -= (a[0] - i)
                i, temp_value_sum = cmp(i, temp_value_sum, type_id, a)

        elif byte_array[i] == '1':
            size = int(byte_array[i + 1:i + 12], 2)
            i += 12

            while size > 0:
                a = get_packet_p2(i, byte_array)
                size -= 1
                i, temp_value_sum = cmp(i, temp_value_sum, type_id, a)

        return i, temp_value_sum


def cmp(i, temp_value_sum, type_id, a):
    i = a[0]

    if type_id == 0:
        temp_value_sum += a[1]
    elif type_id == 1:
        temp_value_sum *= a[1]
    elif type_id == 2:
        if temp_value_sum is None:
            temp_value_sum = a[1]
        else:
            temp_value_sum = min(temp_value_sum, a[1])
    elif type_id == 3:
        if temp_value_sum is None:
            temp_value_sum = a[1]
        else:
            temp_value_sum = max(temp_value_sum, a[1])
    elif type_id == 5:
        if temp_value_sum is None:
            temp_value_sum = a[1]
        else:
            temp_value_sum = 1 if temp_value_sum > a[1] else 0
    elif type_id == 6:
        if temp_value_sum is None:
            temp_value_sum = a[1]
        else:
            temp_value_sum = 1 if temp_value_sum < a[1] else 0
    elif type_id == 7:
        if temp_value_sum is None:
            temp_value_sum = a[1]
        else:
            temp_value_sum = 1 if temp_value_sum == a[1] else 0

    return i, temp_value_sum


def binary_representation_p1(filename):
    with open(filename) as f:
        line = f.readline()

    byte_array = ""
    for i in line:
        byte_array += str(bin(int(i, 16))[2:].zfill(4))

    return get_packet_p2(0, byte_array)[1]


if __name__ == '__main__':
    print(binary_representation_p1("input"))
10626357269192
10622171731507