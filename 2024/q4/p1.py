

def parse_data(in_file: str):
    """
    Returns contents of input file as a two-dimensional list
    :param in_file: Name of input file
    :returns: Two-dimensional list of characters (Strings)
    """
    with open(in_file, 'r') as f:
        return [list(row) for row in str.split('\n')]


def count_word(parsed_data: list[list[str]], word):
    """
    Returns a count of all occurrences of word in parsed_data
    :param parsed_data: List of lists of strings representing input data
    :param word: String word to be searched for in parsed_data
    :returns: Integer
    """
    for c1 in parsed_data:
        if c1 ==


def main(in_file, out_file):
    parsed_data = parse_data(in_file)
    xmas_count = count_word(parsed_data, 'XMAS')


if __name__ == '__main__':
    main('in.txt', 'p1_out.txt')
