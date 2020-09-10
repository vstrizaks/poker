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
    b, suit, hc = check_flush(hand)
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
    for key, val in value_counts.items():
        if val == 4:
            return True, card_order_dict[key]
    return False, 0


def check_full_house(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)

    for v in values:
        value_counts[card_order_dict[v]] += 1
    list_of_keys = []
    high_card = 0
    for key, val in value_counts.items():
        if val >= 3:
            list_of_keys.append(key)
            if key > high_card:
                high_card = key
    if list_of_keys:
        for key, val in value_counts.items():
            if key not in list_of_keys and val >= 2:
                list_of_keys.append(key)

    if len(list_of_keys) >= 2:
        return True, high_card
    else:
        return False, 0


def generate_hand_index(hand):
    values = [i[0] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    rank_values.sort(reverse=True)
    hand_index = 6
    for v in rank_values:
        hand_index *= 100
        hand_index += v
    return hand_index


def flush_find_high_card_fn(hand, suit):
    hand_flush = [val for val in hand if val[1] == suit]
    return generate_hand_index(hand_flush)


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
        suit = "h"
        return True, suit, flush_find_high_card_fn(hand, suit)
    elif d_count >= 5:
        suit = "d"
        return True, suit, flush_find_high_card_fn(hand, suit)
    elif c_count >= 5:
        suit = "c"
        return True, suit, flush_find_high_card_fn(hand, suit)
    elif s_count >= 5:
        suit = "s"
        return True, suit, flush_find_high_card_fn(hand, suit)
    else:
        return False, "n", 0


def check_straight(hand):
    values = [i[0] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    if 14 in rank_values:
        rank_values.append(1)
    rank_values = list(dict.fromkeys(rank_values))
    rank_values.sort(reverse=True)
    cur_val = 0
    counter = 1
    high_card = 0
    for val in rank_values:
        if (cur_val - 1) == val:
            if counter == 1:
                high_card = cur_val
            counter += 1
        else:
            counter = 1
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
        for key, val in value_counts.items():
            if val == 3:
                return (
                    True,
                    card_order_dict[key] * 100000000,
                    find_kicker(hand, [card_order_dict[key]], kicker_count=2),
                )
    else:
        return False, 0, 0


def check_two_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    counter = 0
    first_high_card = 0
    second_high_card = 0
    for key, val in value_counts.items():
        if val == 2:
            counter += 1
            if card_order_dict[key] > first_high_card:
                if first_high_card > second_high_card:
                    second_high_card = first_high_card
                first_high_card = card_order_dict[key]
    if counter >= 2:
        return (
            True,
            first_high_card * 100000000,
            find_kicker(hand, [first_high_card, second_high_card]),
        )
    else:
        return False, 0, 0


def check_one_pairs(hand):
    values = [i[0] for i in hand]
    value_counts = defaultdict(lambda: 0)
    for v in values:
        value_counts[v] += 1
    if 2 in value_counts.values():
        high_card = 0
        for key, val in value_counts.items():
            if val == 2:
                if card_order_dict[key] > high_card:
                    high_card = card_order_dict[key]
        return (
            True,
            high_card * 100000000,
            find_kicker(hand, [high_card], kicker_count=3),
        )
    else:
        return False, 0, 0


def find_kicker(hand, cards_to_skip, kicker_count=1):
    values = [i[0] for i in hand]
    rank_values = [card_order_dict[i] for i in values]
    clean_list = []
    for card in rank_values:
        if card not in cards_to_skip:
            clean_list.append(card)
    clean_list.sort(reverse=True)
    clean_list = clean_list[:kicker_count]
    kicker = 1
    for v in clean_list:
        kicker *= 100
        kicker += v
    return kicker

