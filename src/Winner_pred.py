import numpy as np
import collections


# Pair : 15-29
# Two Pair : 30-44
# Three of a Kind : 45-59
# Straight : 60-74
# Flush : 75-89
# Full House : 90-104
# Four of kind : 105-119
# Straight Flush : 120-134
# Royal Straight Flush : 135
# Default: High Card : 1-14


def helper_get_numbers(hand):
    numbers = []
    for card in hand:
        numbers.append(int(card[1:]))
    return numbers


def helper_get_suit_list(hand):
    suit = []
    for card in hand:
        suit.append(card[0])

    return suit


def check_for_royal_flush(hand):
    suit = helper_get_suit_list(hand)
    str = ''
    for s in suit:
        str += s
    ref_str = str[0] * len(str)

    if str == ref_str:
        numbers = helper_get_numbers(hand)
        numbers.sort()
        np.asarray(numbers)
        if (np.sum(np.diff(numbers)) == 4) and (numbers[0] + numbers[4] == 24):
            return 135
    return 0


def check_for_straight_flush(hand):
    suit = helper_get_suit_list(hand)
    str = ''
    for s in suit:
        str += s
    ref_str = str[0] * len(str)

    if str == ref_str:
        numbers = helper_get_numbers(hand)
        numbers.sort()
        numbers = np.asarray(numbers)
        if np.sum(np.asarray(np.diff(numbers))) == 4:
            return 120 + numbers[-1]
    return 0


def check_four_of_a_kind(hand):
    numbers = helper_get_numbers(hand)
    freq = collections.Counter(numbers)
    if 4 in freq.values():
        for key in freq.keys():
            if freq[key] == 4:
                return 105 + key
    return 0


def check_full_house(hand):
    numbers = helper_get_numbers(hand)
    freq = collections.Counter(numbers)

    if (3 in freq.values()) and (2 in freq.values()):
        for key in freq.keys():
            if freq[key] == 3:
                return 90 + key
    return 0


def check_for_flush(hand):
    suit = helper_get_suit_list(hand)
    str = ''
    for s in suit:
        str += s
    ref_str = str[0] * len(str)

    if str == ref_str:
        numbers = helper_get_numbers(hand)
        numbers.sort(reverse=True)
        score = 75 + numbers[0]
        for i in range(1, 5):
            score += (numbers[i]) / (pow(10, 2 * i))
        return score
    return 0


def check_three_of_a_kind(hand):
    numbers = helper_get_numbers(hand)
    freq = collections.Counter(numbers)
    if 3 in freq.values():
        for key in freq.keys():
            if freq[key] == 3:
                return 45 + key
    return 0


# def check_for_two_pairs(hand):
#     numbers = helper_get_numbers(hand)
#     np.asarray(numbers)
#     freq = collections.Counter(numbers)
#     values_arr = []
#     for key in freq.keys():

## Main

## Sample test for royal flush
# sample_hand0 = ['C10', 'C11', 'C12', 'C14', 'C13']
# print(check_for_royal_flush(sample_hand0))

## Sample test for straight flush
# sample_hand1 = ['C5', 'C6', 'C7', 'C8', 'C4']
# sample_hand2 = ['D4', 'D5', 'D6', 'D7', 'D8']
# print(check_for_straight_flush(sample_hand1))
# print(check_for_straight_flush(sample_hand2))


## Sample test for 4 of a kind
# sample_hand3 = ['C8', 'D8', 'S8', 'H8', 'C12']
# sample_hand4 = ['D5', 'D3', 'C5', 'H5', 'S5']
# print(check_four_of_a_kind(sample_hand3))
# print(check_four_of_a_kind(sample_hand4))


## Sample test for Full House
# sample_hand5 = ['D3', 'D2', 'C3', 'C2', 'H3']
# sample_hand6 = ['D6', 'D8', 'C6', 'C8', 'H9']
# print(check_full_house(sample_hand5))
# print(check_full_house(sample_hand6))


## Sample test for Flush
# sample_hand7 = ['D13', 'D14', 'D11', 'D9', 'D12']
# sample_hand8 = ['C3', 'C4', 'C8', 'C9', 'C12']
# print(check_for_flush(sample_hand7))
# print(check_for_flush(sample_hand8))


## Sample test for 3 of a kind
# sample_hand9 = ['D13', 'C13', 'H13', 'D9', 'D12']
# sample_hand10 = ['H12', 'S2', 'C8', 'C9', 'C12']
# print(check_three_of_a_kind(sample_hand9))
# print(check_three_of_a_kind(sample_hand10))


## Sample test for Two pair
sample_hand11 = ['S8', 'H8', 'C4', 'D6', 'D4']
check_for_two_pairs(sample_hand11)