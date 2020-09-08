from textwrap import wrap
from sys import stdin

from functions import *
from functions import check_two_pairs

for str_line in stdin:
    board = str_line.split(" ", 1)[0]
    hands = str_line.split(" ", 1)[1].split()

    board_list = wrap(board, 2)
    hands_dict = {i: hands[i] for i in range(len(hands))}

    flag_match = False
    result = {}
    result_no_score = {}
    for key, val in hands_dict.items():
        hand = wrap(val, 2)
        board_and_hand = board_list.copy()
        board_and_hand.extend(hand)
        b, high_card = check_straight_flush(board_and_hand)
        if b:
            result[key] = 9
            flag_match = True
            continue

        if check_four_of_a_kind(board_and_hand):
            result[key] = 8
            flag_match = True
            continue

        if check_full_house(board_and_hand):
            result[key] = 7
            flag_match = True
            continue

        b, suit = check_flush(board_and_hand)
        if b:
            result[key] = 6
            flag_match = True
            continue

        b, high_card = check_straight(board_and_hand)
        if b:
            result[key] = 5
            flag_match = True
            continue

        if check_three_of_a_kind(board_and_hand):
            result[key] = 4
            flag_match = True
            continue

        if check_two_pairs(board_and_hand):
            result[key] = 3
            flag_match = True
            continue

        if check_one_pairs(board_and_hand):
            result[key] = 2
            flag_match = True
            continue

        result[key] = 1
        if not flag_match:
            result_no_score[key] = find_high_card(board_and_hand)

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

        if not flag_match:
            result = result + hands_dict[key] + seporator
            continue

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

    print(result)

