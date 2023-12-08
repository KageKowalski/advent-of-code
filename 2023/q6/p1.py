# Imports
from math import sqrt, ceil, floor


# vars
in_file = "in.txt"
out_file = "p1_out.txt"


def get_winning_values_for_race(race):
    """
    Supporting function for calculating winning values of the passed race
    :param race: List containing race data in the format [time, distance]
    :return: A List of Integers representing what values are capable of winning the race
    """
    winning_values = []
    time = race[0]
    distance = race[1]
    for i in range(distance):
        if i * (time - i) > distance:
            winning_values.append(i)

    return winning_values


def get_races(data):
    """
    Supporting function for parsing the passed data
    :param data: List of Strings representing file lines
    :return: List of Lists of Integers, representing data on races, in the format [[time, distance]]
    """
    data[0] = data[0].split()
    data[0].pop(0)
    data[1] = data[1].split()
    data[1].pop(0)
    races = []
    for i in range(len(data[0])):
        races.append([int(data[0][i]), int(data[1][i])])

    return races


def main():
    """
    Main function, as described in Advent of Code 2023 q4
    """
    with open(in_file, 'r') as in_f:
        races = get_races(in_f.readlines())

    output_value = 1
    i = 1
    for race in races:
        i = i + 1
        winning_values = get_winning_values_for_race(race)
        output_value = output_value * len(winning_values)
        print(f'Winning values for race {i}: {winning_values}')

    with open(out_file, 'w') as out_f:
        out_f.write(str(output_value))


# Call main function
if __name__ == "__main__":
    main()
