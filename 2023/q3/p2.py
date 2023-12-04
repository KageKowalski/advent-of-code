# imports
from p1 import convert_txt_data_to_2d_list, pad_schematic


# vars
in_file = "in.txt"
out_file = "p2_out.txt"


def get_part_number(schematic, l_index, c_index):
    """
    Supporting function
    :param schematic: Engine schematic as a 2-dimensional array of Strings
    :param l_index: Line index of a numeral that is part of a number
    :param c_index: Character index of a numeral that is part of a number
    :return: The full part number associated with the numeral at l_index, c_index, as an Integer
    """
    end_c_index = c_index
    while schematic[l_index][end_c_index].isnumeric():
        end_c_index = end_c_index + 1

    start_c_index = c_index
    while schematic[l_index][start_c_index].isnumeric():
        start_c_index = start_c_index - 1

    part_number = ''
    for i in range(start_c_index+1, end_c_index):
        part_number = part_number + schematic[l_index][i]

    return int(part_number)


def get_gear_ratio(schematic, l_index, c_index):
    """
    Supporting function
    :param schematic: Engine schematic as a 2-dimensional array of Strings
    :param l_index: Line index of a gear
    :param c_index: Character index of a gear
    :return: Gear ratio of the passed gear as an Integer
    """
    part_numbers = []
    if schematic[l_index-1][c_index-1].isnumeric():
        part_numbers.append(get_part_number(schematic, l_index-1, c_index-1))
        if schematic[l_index-1][c_index] == '.' and schematic[l_index-1][c_index+1].isnumeric():
            part_numbers.append(get_part_number(schematic, l_index-1, c_index+1))
    elif schematic[l_index-1][c_index].isnumeric():
        part_numbers.append(get_part_number(schematic, l_index-1, c_index))
    elif schematic[l_index-1][c_index+1].isnumeric():
        part_numbers.append(get_part_number(schematic, l_index-1, c_index+1))

    if schematic[l_index][c_index-1].isnumeric():
        part_numbers.append(get_part_number(schematic, l_index, c_index-1))
    if schematic[l_index][c_index+1].isnumeric():
        part_numbers.append(get_part_number(schematic, l_index, c_index+1))

    if schematic[l_index+1][c_index-1].isnumeric():
        part_numbers.append(get_part_number(schematic, l_index+1, c_index-1))
        if schematic[l_index+1][c_index] == '.' and schematic[l_index+1][c_index+1].isnumeric():
            part_numbers.append(get_part_number(schematic, l_index+1, c_index+1))
    elif schematic[l_index+1][c_index].isnumeric():
        part_numbers.append(get_part_number(schematic, l_index+1, c_index))
    elif schematic[l_index+1][c_index+1].isnumeric():
        part_numbers.append(get_part_number(schematic, l_index+1, c_index+1))

    return part_numbers[0] * part_numbers[1]


def is_gear(schematic, l_index, c_index):
    """
    Supporting function
    :param schematic: Engine schematic as a 2-dimensional array of Strings
    :param l_index: Line index of a suspected gear
    :param c_index: Character index of a suspected gear
    :return: True if passed l_index, c_index is a gear, else False
    """
    part_count = 0
    if schematic[l_index-1][c_index-1].isnumeric():
        part_count = part_count + 1
        if schematic[l_index-1][c_index] == '.' and schematic[l_index-1][c_index+1].isnumeric():
            part_count = part_count + 1
    elif schematic[l_index-1][c_index].isnumeric():
        part_count = part_count + 1
    elif schematic[l_index-1][c_index+1].isnumeric():
        part_count = part_count+1

    if schematic[l_index][c_index-1].isnumeric():
        part_count = part_count + 1
    if schematic[l_index][c_index+1].isnumeric():
        part_count = part_count + 1

    if schematic[l_index+1][c_index-1].isnumeric():
        part_count = part_count + 1
        if schematic[l_index+1][c_index] == '.' and schematic[l_index+1][c_index+1].isnumeric():
            part_count = part_count + 1
    elif schematic[l_index+1][c_index].isnumeric():
        part_count = part_count + 1
    elif schematic[l_index+1][c_index+1].isnumeric():
        part_count = part_count+1

    return part_count == 2


def get_gear_ratios(schematic):
    """
    Supporting function
    :param schematic: Engine schematic as a 2-dimensional array of Strings
    :return: List of gear ratios as Integers
    """
    gear_ratios = []
    for l_index, l in enumerate(schematic):
        for c_index, c in enumerate(l):
            if c == '*' and is_gear(schematic, l_index, c_index):
                gear_ratios.append(int(get_gear_ratio(schematic, l_index, c_index)))

    return gear_ratios


def main():
    """
    Main function, as described in Advent of Code 2023 q3
    """
    data = ''
    with open(in_file, 'r') as in_f:
        data = in_f.readlines()
    schematic = convert_txt_data_to_2d_list(data)
    padded_schematic = pad_schematic(schematic)

    gear_ratios = get_gear_ratios(schematic)
    sum_val = 0
    for gear_ratio in gear_ratios:
        sum_val = sum_val + gear_ratio

    with open(out_file, 'w') as out_f:
        out_f.write(str(sum_val))


# Call main function
if __name__ == "__main__":
    main()
