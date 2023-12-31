# vars
in_file = "in.txt"
out_file = "out.txt"


def get_first_numeral(word):
    """
    Supporting function

    :param: word
    :return: The first numeral contained within the passed word as a String, else '-1'
    """
    for c in word:
        if c.isnumeric():
            return c
    return '-1'


def get_last_numeral(word):
    """
    Supporting function

    :param: word
    :return: The last numeral contained within the passed word as a String, else '-1'
    """
    last_numeral = '-1'
    for c in word:
        if c.isnumeric():
            last_numeral = c
    return last_numeral


def main():
    """
    Main function, as described in Advent of Code 2023 q1
    """
    with open(in_file, 'r') as in_f, open(out_file, 'w') as out_f:
        sum_val = 0
        for line in in_f:
            first_numeral = get_first_numeral(line)
            last_numeral = get_last_numeral(line)
            if first_numeral != '-1' and last_numeral != '-1':
                sum_val = sum_val + int(first_numeral + last_numeral)
        out_f.write(str(sum_val))


# Call main function
if __name__ == "__main__":
    main()
