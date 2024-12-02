from p1 import _parse_data


def _sort_data(_parsed_data):
    """
    Sort parsed data into a useful output
    :param _parsed_data: List of two lists representing sorted input data
    :return: Dictionary where keys are left-column unique integers and values are right-column occurence count
    """
    sorted_data = {}
    for n in _parsed_data[0]:
        sorted_data[n] = 0
    for n in _parsed_data[1]:
        if n in sorted_data:
            sorted_data[n] = sorted_data[n] + 1
    return sorted_data


def main():
    in_file = 'in.txt'
    out_file = 'p2_out.txt'

    parsed_data = _parse_data(in_file)
    sorted_data = _sort_data(parsed_data)

    similarity = 0
    for n in sorted_data:
        similarity = similarity + (n * sorted_data[n])

    with open(out_file, 'w') as f:
        f.write(str(similarity))


if __name__ == '__main__':
    main()
