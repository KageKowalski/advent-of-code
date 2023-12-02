# vars
in_file = "in.txt"
out_file = "out.txt"


def get_power(game):
    """
    Supporting function
    :param game: The full input line for one game
    :type game: String
    :return: The power of the minimum amount of cubes necessary for the game to be possible
    :rtype: int
    """
    power = 0
    handfuls = game.split(': ')[1].split('\n')[0].split('; ')
    largest_red = 0
    largest_green = 0
    largest_blue = 0
    for handful in handfuls:
        separated_handful = handful.split(', ')
        for amount_color in separated_handful:
            amount_color = amount_color.split()
            if amount_color[1] == 'red' and int(amount_color[0]) > largest_red:
                largest_red = int(amount_color[0])
            elif amount_color[1] == 'green' and int(amount_color[0]) > largest_green:
                largest_green = int(amount_color[0])
            elif amount_color[1] == 'blue' and int(amount_color[0]) > largest_blue:
                largest_blue = int(amount_color[0])
    power = power + (largest_red * largest_green * largest_blue)

    return power


def main():
    """
    Main function, as described in Advent of Code 2023 q2
    """
    with open(in_file, 'r') as in_f:
        sum_val = 0
        for line in in_f:
            sum_val = sum_val + get_power(line)

    with open(out_file, 'w') as out_f:
        out_f.write(str(sum_val))


# Call main function
if __name__ == "__main__":
    main()
