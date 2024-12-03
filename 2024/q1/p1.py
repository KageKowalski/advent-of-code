def parse_data(_in_file):
    """
    Parses data from input file into two lists
    :param _in_file: Name of the input file
    :return: List of two lists
    """
    l1 = []
    l2 = []
    with open(_in_file, 'r') as f:
        for line in f:
            val1, val2 = line.strip().split()
            l1.append(int(val1))
            l2.append(int(val2))
    return [l1, l2]


def calculate_distance(_sorted_data):
    """
    Calculate distance of passed sorted data
    :param _sorted_data: List of two lists representing sorted input data
    :return: Integer value representing distance of data in _sorted_data
    """
    distance = 0
    for i in range(0, len(_sorted_data[0])):
        distance = distance + (abs(_sorted_data[0][i] - _sorted_data[1][i]))
    return distance


def main():
    in_file = 'in.txt'
    out_file = 'p1_out.txt'

    parsed_data = parse_data(in_file)
    sorted_data = [sorted(parsed_data[0]), sorted(parsed_data[1])]

    with open(out_file, 'w') as f:
        f.write(str(calculate_distance(sorted_data)))


if __name__ == '__main__':
    main()
