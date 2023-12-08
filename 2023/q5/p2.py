# Imports
from p1 import map_id, map_seed_to_location, get_maps
from math import inf


# vars
in_file = "in.txt"
out_file = "p2_out.txt"


def get_seeds(data):
    seeds_info = data.split('\n\n')[0].split(': ')[1].split()
    seeds = []
    for i in range(len(seeds_info)):
        seeds_info[i] = int(seeds_info[i])
        if i % 2 == 1:
            print(f'Adding seed range: {i / 2}')
            for seed in range(seeds_info[i-1], seeds_info[i-1] + seeds_info[i]):
                seeds.append(seed)
    return seeds


def main():
    """
    Main function, as described in Advent of Code 2023 q4
    """
    with open(in_file, 'r') as in_f:
        data = in_f.read()
    seeds = get_seeds(data)
    maps = get_maps(data)

    lowest_location_number = inf
    print(f'There are {len(seeds)} seeds.')
    for seed in seeds:
        i = 0
        print(f'Seeds processed: {float(i) / float(len(seeds)) * 100}%')
        location = map_seed_to_location(seed, maps)
        if location < lowest_location_number:
            lowest_location_number = location
        i = i + 1

    with open(out_file, 'w') as out_f:
        out_f.write(str(lowest_location_number))


# Call main function
if __name__ == "__main__":
    main()
