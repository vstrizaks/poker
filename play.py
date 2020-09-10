from textwrap import wrap
from sys import stdin

from functions import *
from functions import check_two_pairs


def play_poker(board, hands, test_run=False):
    board_list = wrap(board, 2)
    hands_dict = {i: hands[i] for i in range(len(hands))}

    multiplier = 10000000000

    flag_match = False
    result = {}
    result_no_score = {}
    for key, val in hands_dict.items():
        hand = wrap(val, 2)
        board_and_hand = board_list.copy()
        board_and_hand.extend(hand)
        b, high_card = check_straight_flush(board_and_hand)
        if b:
            result[key] = 9 * multiplier + high_card
            flag_match = True
            continue

        b, high_card = check_four_of_a_kind(board_and_hand)
        if b:
            result[key] = 8 * multiplier + high_card
            flag_match = True
            continue

        b, high_card = check_full_house(board_and_hand)
        if b:
            result[key] = 7 * multiplier + high_card
            flag_match = True
            continue

        b, suit, hand_index = check_flush(board_and_hand)
        if b:
            result[key] = hand_index
            flag_match = True
            continue

        b, high_card = check_straight(board_and_hand)
        if b:
            result[key] = 5 * multiplier + high_card
            flag_match = True
            continue

        b, high_card, kicker = check_three_of_a_kind(board_and_hand)
        if b:
            result[key] = 4 * multiplier + high_card + kicker
            flag_match = True
            continue

        b, high_card_in_combination, kicker = check_two_pairs(board_and_hand)
        if b:
            result[key] = (3 * multiplier) + high_card_in_combination + kicker
            flag_match = True
            continue

        b, high_card_in_combination, kicker = check_one_pairs(board_and_hand)
        if b:
            result[key] = 2 * multiplier + high_card_in_combination + kicker
            flag_match = True
            continue

        result[key] = 1 * multiplier
        if not flag_match:
            result_no_score[key] = find_kicker(board_and_hand, [], kicker_count=5)

    if flag_match:
        sorted_hands = {
            k: v for k, v in sorted(result.items(), key=lambda item: item[1])
        }
    else:
        sorted_hands = {
            k: v for k, v in sorted(result_no_score.items(), key=lambda item: item[1])
        }

    result = ""
    pos = 0
    sorted_hands_list = list(sorted_hands.values())
    equal_list = []
    for key in sorted_hands.keys():
        seporator = " "

        if key != int(list(sorted_hands.keys())[-1]):
            if sorted_hands_list[pos] == sorted_hands_list[pos + 1]:
                equal_list.append(hands_dict[key])
                pos += 1
                continue
        pos += 1
        if equal_list:
            equal_list.append(hands_dict[key])
            sorted_list = sorted(equal_list)
            for l in sorted_list:
                if l != sorted_list[-1]:
                    seporator = "="
                else:
                    seporator = " "
                result = result + l + seporator
            equal_list = []
        else:
            result = result + hands_dict[key] + seporator

    if test_run:
        return result.rstrip()
    else:
        print(result.rstrip())


def main():
    for str_line in stdin:
        try:
            board = str_line.split(" ", 1)[0]
            hands = str_line.split(" ", 1)[1].split()
        except Exception:
            print("Incorrect input. Example: 4cKs4h8s7s Ad4s Ac4d As9s KhKd 5d6d")
            continue

        play_poker(board, hands)


if __name__ == "__main__":
    main()
