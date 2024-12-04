import re


def parse_data(in_file):
    with open(in_file, 'r') as f:
        return re.findall(r'mul\(\d+,\d+\)', f.read())


def sum_muls(muls: list[str]):
    s = 0
    for mul in muls:
        nums = re.findall(r'\d+', mul)
        s = s + (int(nums[0]) * int(nums[1]))
    return s


def main(in_file: str, out_file: str):
    with open(out_file, 'w') as f:
        f.write(str(sum_muls(parse_data(in_file))))


if __name__ == '__main__':
    main('in.txt', 'p1_out.txt')
