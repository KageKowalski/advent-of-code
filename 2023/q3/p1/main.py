# vars
in_file = "in.txt"
out_file = "out.txt"


def pad_schematic(schematic):
    """
    Supporting function
    :param schematic: Engine schematic as a list of lists
    :return: The passed schematic but with its perimeter padded with '.' values
    """
    for i in range(len(schematic)):
        schematic[i].insert(0, '.')
        schematic[i].insert(len(schematic)+1, '.')

    empty_line = []
    for i in range(len(schematic[0])):
        empty_line.append('.')

    schematic.insert(0, empty_line)
    schematic.insert(len(schematic), empty_line)

    return schematic


def find_full_number(schematic, l_index, c_index):
    """
    Supporting function
    :param schematic: Engine schematic as a list of lists
    :param l_index: Index of a line
    :param c_index: Index of a character
    :return: Coordinates of the character index of the last numeral that is part of the passed coordinates' number
    """
    if not schematic[l_index][c_index + 1].isnumeric():
        return c_index
    else:
        return find_full_number(schematic, l_index, c_index + 1)


def touches_symbol(schematic, l_index, c_index):
    """
    Supporting function
    :param schematic: Engine schematic as a list of lists
    :param l_index: Index of a line
    :param c_index: Index of a character
    :return: True if passed l_index,c_index coordinate touches a symbol, else False
    """
    return (is_symbol(schematic[l_index - 1][c_index - 1]) or is_symbol(schematic[l_index - 1][c_index]) or
            is_symbol(schematic[l_index - 1][c_index + 1]) or is_symbol(schematic[l_index][c_index - 1]) or
            is_symbol(schematic[l_index][c_index + 1]) or is_symbol(schematic[l_index + 1][c_index - 1]) or
            is_symbol(schematic[l_index + 1][c_index]) or is_symbol(schematic[l_index + 1][c_index + 1]))


def is_symbol(str_val):
    """
    Supporting function
    :param str_val: String value
    :return: True if passed value is a symbol, else False
    """
    return not str_val.isnumeric() and not str_val == '.'


def convert_txt_data_to_2d_list(data):
    """
    Supporting function
    :param data: String representing the contents of a txt file
    :return: data parameter reformatted as a list of lists
    """
    list_of_lists = []
    for l_index, l in enumerate(data):
        list_of_lists.append([])
        for c_index, c in enumerate(l.strip('\n')):
            list_of_lists[l_index].append([])
            list_of_lists[l_index][c_index] = c

    return list_of_lists


def get_engine_parts(schematic):
    """
    Supporting Function
    :param schematic: Engine schematic as a 2-dimensional array of Strings
    :return: List of engine part numbers as Integers
    """
    engine_parts = []
    for l_index, l in enumerate(schematic):
        for c_index, c in enumerate(l):
            if c.isnumeric() and not schematic[l_index][c_index-1].isnumeric():
                last_numeral = find_full_number(schematic, l_index, c_index)
                number_is_valid = False
                number = ''
                for i in range(c_index, last_numeral+1):
                    number = number + schematic[l_index][i]
                    if touches_symbol(schematic, l_index, i):
                        number_is_valid = True
                if number_is_valid:
                    engine_parts.append(int(number))

    return engine_parts


def main():
    """
    Main function, as described in Advent of Code 2023 q3
    """
    data = ''
    with open(in_file, 'r') as in_f:
        data = in_f.readlines()
    schematic = convert_txt_data_to_2d_list(data)
    padded_schematic = pad_schematic(schematic)
    print(padded_schematic)

    engine_parts = get_engine_parts(padded_schematic)
    sum_val = 0
    for engine_part in engine_parts:
        sum_val = sum_val + engine_part

    with open(out_file, 'w') as out_f:
        out_f.write(str(sum_val))


# Call main function
if __name__ == "__main__":
    main()
