import re


def parse_data(in_file: str) -> (dict[int, list[int]], list[list[int]]):
    instr_dict = {}
    update_list = []

    with open(in_file, 'r') as f:
        data = f.read().split('\n\n')
    assert(len(data) == 2) # First index should be instructions, second index should be updates

    # Populate instr_dict where keys are numbers and values are a list of numbers that must come after the key
    for raw_instr in data[0].split('\n'):
        instr_digits = re.findall(r'\d+', raw_instr)
        assert(len(instr_digits) == 2) # Instruction should consist of exactly 2 digits
        if instr_digits[0] not in instr_dict:
            instr_dict[instr_digits[0]] = []
            instr_dict[instr_digits[0]].append(instr_digits[1])
        else:
            instr_dict[instr_digits[0]].append(instr_digits[1])

    # Populate update_list as a list of updates, each of which is a list of numbers
    # TODO - Fix this part, not working
    for raw_update in data[1].split('\n'):
        nums = int(num) for num in re.findall(r'\d+', raw_update)
        update_list.append(nums)

    return instr_dict, update_list


def main(in_file: str, out_file: str):
    parsed_data = parse_data(in_file)


if __name__ == '__main__':
    main('p1_simple_in.txt', 'p1_out.txt')
