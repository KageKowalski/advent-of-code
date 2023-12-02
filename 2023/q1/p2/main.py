# imports
from math import inf

# vars
in_file = "in.txt"
out_file = "out.txt"


# Supporting function, returns numerical representation of passed word as a String, else returns original value
def convert_numeral(numeral):
    if numeral == 'one':
        return '1'
    if numeral == 'two':
        return '2'
    if numeral == 'three':
        return '3'
    if numeral == 'four':
        return '4'
    if numeral == 'five':
        return '5'
    if numeral == 'six':
        return '6'
    if numeral == 'seven':
        return '7'
    if numeral == 'eight':
        return '8'
    if numeral == 'nine':
        return '9'
    return numeral


# Supporting function, returns the first numeral contained within the passed word as a String, else '-1'
def get_first_numeral(word):
    numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                'eight', 'nine']

    first_numeral = '-1'
    first_numeral_index = inf
    for numeral in numerals:
        try:
            if int(word.index(numeral)) < first_numeral_index:
                first_numeral = numeral
                first_numeral_index = word.index(numeral)
        except ValueError:
            pass

    print(f'Word: {word} First Numeral: {first_numeral}')
    return convert_numeral(first_numeral)


# Supporting function, returns the last numeral contained within the passed word as a String, else '-1'
def get_last_numeral(word):
    numerals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
                'eight', 'nine']

    last_numeral = '-1'
    last_numeral_index = -inf
    for numeral in numerals:
        try:
            if int(word.rindex(numeral)) > last_numeral_index:
                last_numeral = numeral
                last_numeral_index = word.rindex(numeral)
        except ValueError:
            pass

    print(f'Word: {word} Last Numeral: {last_numeral}')
    return convert_numeral(last_numeral)


# Main function, as described in Advent of Code 2023 q1
def main():
    with open(in_file, 'r') as in_f, open(out_file, 'w') as out_f:
        sum_val = 0
        for line in in_f:
            first_numeral = get_first_numeral(line)
            last_numeral = get_last_numeral(line)
            if first_numeral != '-1' and last_numeral != '-1':
                sum_val = sum_val + int(first_numeral + last_numeral)
        out_f.write(str(sum_val))


# Call main function
if __name__ == "__main__":
    main()
