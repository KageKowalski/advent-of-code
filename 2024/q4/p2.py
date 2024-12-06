from p1 import parse_data


def xmas_exists(parsed_data: list[list[str]], root_coords: (int,int)) -> bool:
    xmas_count = 0
    for ri in [-1,1]:
        for ci in [-1,1]:
            if -1 < root_coords[0] + ri < len(parsed_data) and \
                    -1 < root_coords[1] + ci < len(parsed_data[root_coords[0]]) and \
                    parsed_data[root_coords[0] + ri][root_coords[1] + ci] == 'M' and \
                    -1 < root_coords[0] - ri < len(parsed_data) and \
                    -1 < root_coords[1] - ci < len(parsed_data[root_coords[0]]) and \
                    parsed_data[root_coords[0] - ri][root_coords[1] - ci] == 'S':
                xmas_count = xmas_count + 1
    return xmas_count > 1


def count_mas(parsed_data: list[list[str]]) -> int:
    mas_found = 0
    for r in range(len(parsed_data)):
        for c in range(len(parsed_data[r])):
            if parsed_data[r][c] == 'A':
                if xmas_exists(parsed_data, (r,c)):
                    mas_found = mas_found + 1
    return mas_found


def main(in_file, out_file):
    parsed_data = parse_data(in_file)
    mas_count = count_mas(parsed_data)

    with open(out_file, 'w') as f:
        f.write(str(mas_count))


if __name__ == '__main__':
    main('in.txt', 'p2_out.txt')
