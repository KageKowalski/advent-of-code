# vars
in_file = "in.txt"
out_file = "out.txt"
red_max = 12
green_max = 13
blue_max = 14


def game_is_possible(game):
    """
    Supporting function
    :param game: The full input line for one game
    :type game: String
    :return: If game is possible, returns game number, else 0
    :rtype: int
    """
    game_number = game.split(': ')[0].split()[1]

    handfuls = game.split(': ')[1].split('\n')[0].split('; ')
    for handful in handfuls:
        separated_handful = handful.split(', ')
        print(separated_handful)
        for amount_color in separated_handful:
            amount_color = amount_color.split()
            if amount_color[1] == 'red' and int(amount_color[0]) > red_max:
                return 0
            elif amount_color[1] == 'green' and int(amount_color[0]) > green_max:
                return 0
            elif amount_color[1] == 'blue' and int(amount_color[0]) > blue_max:
                return 0

    return int(game_number)


def main():
    """
    Main function, as described in Advent of Code 2023 q2
    """
    with open(in_file, 'r') as in_f:
        sum_val = 0
        for line in in_f:
            sum_val = sum_val + game_is_possible(line)

    with open(out_file, 'w') as out_f:
        out_f.write(str(sum_val))


# Call main function
if __name__ == "__main__":
    main()
