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
        if int(instr_digits[0]) not in instr_dict:
            instr_dict[int(instr_digits[0])] = []
            instr_dict[int(instr_digits[0])].append(int(instr_digits[1]))
        else:
            instr_dict[int(instr_digits[0])].append(int(instr_digits[1]))

    # Populate update_list as a list of updates, each of which is a list of numbers
    for raw_update in data[1].split('\n'):
        str_nums = re.findall(r'\d+', raw_update)
        nums = []
        for str_num in str_nums:
            nums.append(int(str_num))
        update_list.append(nums)

    return instr_dict, update_list


def validate_update(update: list[int], instr_dict: dict[int, list[int]]) -> int:
    for num in update:
        try:
            instrs = instr_dict[num]
        except KeyError:
            pass
        for instr_num in instrs:
            try:
                if update.index(instr_num) < update.index(num):
                    return -1
            except ValueError:
                pass

    return update[len(update)//2]


def main(in_file: str, out_file: str):
    instr_dict, update_list = parse_data(in_file)

    sum_valid_updates = 0
    for update in update_list:
        update_val = validate_update(update, instr_dict)
        if update_val != -1:
            sum_valid_updates = sum_valid_updates + update_val

    with open(out_file, 'w') as f:
        f.write(str(sum_valid_updates))


if __name__ == '__main__':
    main('in.txt', 'p1_out.txt')
