# vars
in_file = "in.txt"
out_file = "p1_out.txt"


def get_ticket_value(ticket):
    """
    Supporting function
    :param ticket: A single line denoting a ticket's information
    :return: The value of the passed ticket as an Integer
    """
    ticket_value = 1
    winning_numbers = ticket.split(': ')[1].split(' | ')[0].split()
    my_numbers = ticket.split(': ')[1].split(' | ')[1].split()
    print(f'Winning Numbers: {winning_numbers}')
    print(f'My Numbers: {my_numbers}')

    win_count = 0
    for my_number in my_numbers:
        if my_number in winning_numbers:
            win_count = win_count + 1

    if win_count == 0:
        return 0
    elif win_count == 1:
        return 1
    else:
        for i in range(win_count-1):
            ticket_value = ticket_value * 2

    print(f'Ticket Value: {ticket_value}')

    return ticket_value


def main():
    """
    Main function, as described in Advent of Code 2023 q4
    """
    ticket_values = []
    with open(in_file, 'r') as in_f:
        for line in in_f:
            ticket_values.append(get_ticket_value(line.strip('\n')))

    sum_val = 0
    for ticket_value in ticket_values:
        sum_val = sum_val + ticket_value

    with open(out_file, 'w') as out_f:
        out_f.write(str(sum_val))


# Call main function
if __name__ == "__main__":
    main()
