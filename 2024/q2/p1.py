def parse_data(_in_file):
    parsed_data = []
    with open(_in_file, 'r') as f:
        for line in f:
            parsed_line = line.strip().split()
            int_parsed_line = []
            for val in parsed_line:
                int_parsed_line.append(int(val))
            parsed_data.append(int_parsed_line)
    return parsed_data


def is_sequential(report):
    if report[0] == report[1]:
        return False

    ascending = False
    if report[0] < report[1]:
        ascending = True

    if ascending:
        for i in range(2, len(report)):
            if report[i-1] > report[i]:
                return False
    else:
        for i in range(2, len(report)):
            if report[i-1] < report[i]:
                return False
    return True


def satisfies_range(report):
    for i in range(1, len(report)):
        if abs(report[i-1] - report[i]) < 1:
            return False
        elif abs(report[i-1] - report[i]) > 3:
            return False
    return True


def main():
    in_file = 'in.txt'
    out_file = 'p1_out.txt'

    parsed_data = parse_data(in_file)

    safe_reports = 0
    for report in parsed_data:
        if is_sequential(report) and satisfies_range(report):
            safe_reports = safe_reports + 1

    with open(out_file, 'w') as f:
        f.write(str(safe_reports))


if __name__ == '__main__':
    main()
