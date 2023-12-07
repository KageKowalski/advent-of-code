# imports
from math import inf


# vars
in_file = "in.txt"
out_file = "p1_out.txt"


def map_id(identifier, m):
    for data_line in m:
        destination_range_start = data_line[0]
        source_range_start = data_line[1]
        range_length = data_line[2]

        if source_range_start <= identifier < source_range_start + range_length:
            return destination_range_start + (identifier - source_range_start)

    return identifier


def map_seed_to_location(seed, maps):
    identifier = seed
    for m in maps:
        identifier = map_id(identifier, m)

    return identifier


def main():
    """
    Main function, as described in Advent of Code 2023 q4
    """
    maps = ''
    seeds = []
    with open(in_file, 'r') as in_f:
        seeds = in_f.readline().strip('\n').split(': ')[1].split()
        in_f.readline()
        maps = in_f.read().split('\n\n')

    for i in range(len(maps)):
        maps[i] = maps[i].split(':\n')[1].split('\n')
        for j in range(len(maps[i])):
            maps[i][j] = maps[i][j].split()
            for k in range(len(maps[i][j])):
                maps[i][j][k] = int(maps[i][j][k])

    lowest_location_number = inf
    for seed in seeds:
        print(f'Mapping seed: {seed}')
        location = map_seed_to_location(int(seed), maps)
        if location < lowest_location_number:
            lowest_location_number = location

    with open(out_file, 'w') as out_f:
        out_f.write(str(lowest_location_number))


# Call main function
if __name__ == "__main__":
    main()
