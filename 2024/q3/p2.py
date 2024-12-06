import re


def main(in_file: str, out_file: str):
    total = 0
    pattern = r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)'

    with open(in_file, 'r') as f:
        parsed_data = re.findall(pattern, f.read())

    recording = True
    for instr in parsed_data:
        if re.match(r'do\(\)', instr):
            recording = True
        elif re.match(r'don\'t\(\)', instr):
            recording = False
        elif recording:
            nums = re.findall(r'\d+', instr)
            total = total + (int(nums[0]) * int(nums[1]))

    with open(out_file, 'w') as f:
        f.write(str(total))


if __name__ == '__main__':
    main('in.txt', 'p2_out.txt')
