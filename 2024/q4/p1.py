def parse_data(in_file: str) -> list[list[str]]:
    with open(in_file, 'r') as f:
        return [list(row) for row in f.read().split('\n')]


def complete_word(parsed_data: list[list[str]], word: str, root_coords: (int,int), letter: int, direction: (int,int)) -> bool:
    if len(word) == letter:
        return True
    letter_coords = (root_coords[0] + (direction[0] * letter), root_coords[1] + (direction[1] * letter))
    try:
        if word[letter:letter+1] == parsed_data[letter_coords[0]][letter_coords[1]]:
            return complete_word(parsed_data, word, root_coords, letter+1, direction)
    except IndexError:
        return False
    return False


def find_first_neighbors(parsed_data: list[list[str]], word: str, root_coords: (int,int)) -> list[(int,int)]:
    first_neighbors = []
    for ri in range(-1, 2):
        for ci in range(-1, 2):
            try:
                if parsed_data[root_coords[0] + ri][root_coords[1] + ci] == word[1:2] and ri != 0 and ci != 0:
                    first_neighbors.append((ri,ci))
            except IndexError:
                pass
    return first_neighbors


def count_word(parsed_data: list[list[str]], word: str) -> int:
    words_found = 0
    for r in range(len(parsed_data)):
        for c in range(len(parsed_data[r])):
            if parsed_data[r][c] == word[:1]:
                first_neighbors = find_first_neighbors(parsed_data, word, (r,c))
                for f_n in first_neighbors:
                    if complete_word(parsed_data, word, (r,c), 2, (f_n[0] - r, f_n[1] - c)):
                        words_found = words_found + 1
    return words_found


def main(in_file, out_file, word):
    assert(len(word) > 2)
    parsed_data = parse_data(in_file)
    word_count = count_word(parsed_data, word)

    with open (out_file, 'w') as f:
        f.write(str(word_count))


if __name__ == '__main__':
    main('simple_in.txt', 'p1_out.txt', 'XMAS')
