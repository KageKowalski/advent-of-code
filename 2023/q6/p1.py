# Imports
from math import sqrt, ceil


# vars
in_file = "in.txt"
out_file = "p1_out.txt"


def get_winning_values_for_race(race):
    """
    Supporting function for calculating winning values of the passed race
    :param race: List containing race data in the format [time, distance]
    :return: A List of Integers representing what values are capable of winning the race
    """
    time = float(race[0])
    distance = float(race[1])
    # distance > time_spent_waiting * (time - time_spent_waiting)
    # d > x * (t - x)
    # x < (t - √(t^2 - 4d)) / 2 OR x > (t + √(t^2 - 4d)) / 2
    time_spent_waiting_less_than = (time - sqrt(time**2 - (4 * distance))) / 2.0
    time_spent_waiting_greater_than = (time + sqrt(time**2 - (4 * distance))) / 2.0

    return range(ceil(time_spent_waiting_less_than), ceil(time_spent_waiting_greater_than))


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
        winning_values = get_winning_values_for_race(race)
        output_value = output_value * len(winning_values)
        print(f'Winning values for race {i}: {winning_values}')
        i = i + 1

    with open(out_file, 'w') as out_f:
        out_f.write(str(output_value))


# Call main function
if __name__ == "__main__":
    main()
