from p1 import parse_data


def fix_update(update: list[int], instr_dict: dict[int, list[int]]) -> int:
    fixed_update = []

    while len(update) > 0:
        for num in update:
            num_is_good = True
            for instr_num in instr_dict[num]:
                print(f'update: {update}\nnum: {num}\ninstr_num: {instr_num}\nupdate.index(num): {update.index(num)}\nupdate.index(instr_num): {update.index(instr_num)}\n\n')
                if update.index(num) > update.index(instr_num):
                    print('Flag4')
                    num_is_good = False
            if num_is_good:
                fixed_update.append(num)
                update.remove(num)
                print(f'This update has been fixed: {update}')
                print(f'It was fixed to: {fixed_update}')
                print(f'The return value is {fixed_update[len(fixed_update)//2]}')

    return fixed_update[len(fixed_update)//2]


def validate_update(update: list[int], instr_dict: dict[int, list[int]]) -> int:
    for num in update:
        try:
            instrs = instr_dict[num]
        except KeyError:
            pass
        for instr_num in instrs:
            try:
                if update.index(instr_num) < update.index(num):
                    return fix_update(update, instr_dict)
            except ValueError:
                pass

    return -1


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
    main('simple_in.txt', 'p2_out.txt')
