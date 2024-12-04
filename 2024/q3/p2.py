import re
from p1 import sum_muls


def format_data(in_file: str):
    formatted_data = ''
    with open(in_file, 'r') as f:
        for line in f:
            if not line.startswith('do()'):
                formatted_data = formatted_data + 'do()'
            formatted_data = formatted_data + line[:len(line)-1]
            if not line.endswith('don\'t()'):
                formatted_data = formatted_data + 'don\'t()' + '\n'
    return formatted_data


def parse_data(formatted_data: str):
    parsed_data = []
    matches = re.finditer(r'^do\(\).*don\'t\(\)', formatted_data)
    for match in matches:
        print(match.group())
        for mul in re.findall(r'mul\(\d+,\d+\)', match.group()):
            parsed_data.append(mul)
    return parsed_data


def main(in_file: str, out_file: str):
    with open(out_file, 'w') as f:
        f.write(str(sum_muls(parse_data(format_data(in_file)))))


if __name__ == '__main__':
    main('in.txt', 'p2_out.txt')
