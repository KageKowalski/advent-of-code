from p1 import parse_data, is_sequential, satisfies_range

def main():
    in_file = 'in.txt'
    out_file = 'p2_out.txt'

    parsed_data = parse_data(in_file)

    safe_reports = 0
    for report in parsed_data:
        report_is_safe = False
        if is_sequential(report) and satisfies_range(report):
            report_is_safe = True
        else:
            for i in range(len(report)):
                if is_sequential(report[:i] + report[i+1:]) and satisfies_range(report[:i] + report[i+1:]):
                    report_is_safe = True
                    break
        if report_is_safe:
            safe_reports = safe_reports + 1


    with open(out_file, 'w') as f:
        f.write(str(safe_reports))


if __name__ == '__main__':
    main()
