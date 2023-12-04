# vars
in_file = "in.txt"
out_file = "p2_out.txt"


def get_ticket_value(ticket):
    """
    Supporting function
    :param ticket: String representing a single ticket, including my numbers and winning numbers
    :return: Integer representing the value of the passed ticket
    """
    ticket_value = 0
    my_numbers, winning_numbers = ticket.split(' | ')[0].split(), ticket.split(' | ')[1].split()
    for my_number in my_numbers:
        if my_number in winning_numbers:
            ticket_value = ticket_value + 1

    return ticket_value


def main():
    """
    Main function, as described in Advent of Code 2023 q4
    """
    card_counts = []
    ticket_values = []
    with open(in_file, 'r') as in_f:
        i = 0
        for line in in_f:
            i = i + 1
            card_counts.append(1)
            ticket_values.append(get_ticket_value(line.strip('\n').split(': ')[1]))

    for ticket_index, ticket_value in enumerate(ticket_values):
        for i in range(card_counts[ticket_index]):
            for j in range(ticket_value):
                card_counts[ticket_index+j+1] = card_counts[ticket_index+j+1] + 1

    card_count_total = 0
    for card_count in card_counts:
        card_count_total = card_count_total + card_count

    with open(out_file, 'w')as out_f:
        out_f.write(str(card_count_total))


# Call main function
if __name__ == "__main__":
    main()
