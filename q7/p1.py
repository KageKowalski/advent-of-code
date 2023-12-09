# imports
from functools import total_ordering


# vars
in_file = "in.txt"
out_file = "p1_out.txt"


@total_ordering
class Hand:
    def __init__(self, cards: str):
        key = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13,
               'A': 14}
        self.cards = []
        for card in cards:
            self.cards.append(key[card])

    def __str__(self):
        return str(self.cards)

    def __repr__(self):
        return str(self.cards)

    def __gt__(self, other):
        my_key = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        other_key = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0}
        for card in self.cards:
            my_key[card] = my_key[card] + 1
        for card in other.cards:
            other_key[card] = other_key[card] + 1
        # One Hand has 5 of a Kind
        if (5 in my_key.values()) ^ (5 in other_key.values()):
            return 5 in my_key.values()
        # One Hand has 4 of a Kind
        if (4 in my_key.values()) ^ (4 in other_key.values()):
            return 4 in my_key.values()
        # One Hand has a Full House
        if (3 in my_key.values() and 2 in my_key.values()) ^ (3 in other_key.values() and 2 in other_key.values()):
            return 3 in my_key.values() and 2 in my_key.values()
        # One Hand has 3 of a Kind
        if (3 in my_key.values()) ^ (3 in other_key.values()):
            return 3 in my_key.values()
        # One Hand has Two Pair
        my_twos = 0
        other_twos = 0
        for my_val, other_val in zip(my_key.values(), other_key.values()):
            if my_val == 2:
                my_twos = my_twos + 1
            if other_val == 2:
                other_twos = other_twos + 1
        if (my_twos == 2) ^ (other_twos == 2):
            return my_twos == 2
        # One Hand has One Pair
        if (2 in my_key.values()) ^ (2 in other_key.values()):
            return 2 in my_key.values()
        # All other cases: High Card wins
        for my_card, other_card in zip(self.cards, other.cards):
            if my_card != other_card:
                return my_card > other_card
        # Return false if Hands are the same
        return False

    def __eq__(self, other):
        return not self > other and not other > self

    def __lt__(self, other):
        return not self > other


def parse_data(data):
    """
    Supporting function to parse data
    :param data: String representing input data
    :return: [[Hand: Hand, Bid: Integer]]
    """
    data = data.split('\n')
    game_info = []
    for line in data:
        game_info.append(line.split())
    for i in range(len(game_info)):
        game_info[i][0] = Hand(game_info[i][0])
        game_info[i][1] = int(game_info[i][1])
    return game_info


def main():
    """
    Main function, as described in Advent of Code 2023 q4
    """
    with open(in_file, 'r') as in_f:
        game_info = parse_data(in_f.read())

    game_info = sorted(game_info, key=lambda hand_bid: hand_bid[0])

    total = 0
    for i, h_b in enumerate(game_info):
        total = total + (h_b[1] * (i + 1))

    with open(out_file, 'w') as out_f:
        out_f.write(str(total))


# Call main function
if __name__ == "__main__":
    main()
