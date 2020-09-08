from collections import defaultdict

card_order_dict = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


def check_straight_flush(hand):
    b, suit = check_flush(hand)
    if b:
        new_hand = [val for val in hand if val[1] == suit]
        b2, high_card = check_straight(new_hand)
        if b2:
            return True, high_card
    return False, 0


def check_four_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if (
        4 in value_counts.values()
        or 5 in value_counts.values()
        or 6 in value_counts.values()
        or 7 in value_counts.values()
    ):
        return True
    return False


def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    list_of_keys = []
    for key, val in value_counts.items():
        if val >= 3:
            list_of_keys.append(key)
    if list_of_keys:
        for key, val in value_counts.items():
            if key not in list_of_keys and val >= 2:
                list_of_keys.append(key)

    if len(list_of_keys) >= 2:
        return True
    else:
        return False


def check_flush(hand):
    suits = [i[1] for i in hand]
    h_count = 0
    d_count = 0
    c_count = 0
    s_count = 0

    for s in suits:
        if s == "h":
            h_count += 1
        elif s == "d":
            d_count += 1
        elif s == "c":
            c_count += 1
        elif s == "s":
            s_count += 1

    if h_count >= 5:
        return True, "h"
    elif d_count >= 5:
        return True, "d"
    elif c_count >= 5:
        return True, "c"
    elif s_count >= 5:
        return True, "s"
    else:
        return False, "n"


def check_straight(hand):
    values = [i[0] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    if 14 in rank_values:
        rank_values.append(1)
    rank_values.sort(reverse=True)
    cur_val = 0
    counter = 1
    high_card = 0
    for val in rank_values:
        if (cur_val - 1) == val:
            if counter == 1:
                high_card = cur_val
            counter += 1

        cur_val = val

        if counter == 5:
            return True, high_card
    return False, 0


def check_three_of_a_kind(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if set(value_counts.values()) == set([3, 1]):
        return True
    else:
        return False


def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    counter = 0
    for key, val in value_counts.items():
        if val == 2:
            counter += 1
    if counter >= 2:
        return True
    else:
        return False


def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if 2 in value_counts.values():
        return True
    else:
        return False


def find_high_card(hand):
    values = [i[0] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    rank_values.sort()
    return rank_values[0]

