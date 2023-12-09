# imports
from p1 import get_winning_values_for_race


# vars
in_file = "in.txt"
out_file = "p2_out.txt"


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

    time = ''
    for time_component in data[0]:
        time = time + time_component

    distance = ''
    for distance_component in data[1]:
        distance = distance + distance_component

    return [[int(time), int(distance)]]


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
