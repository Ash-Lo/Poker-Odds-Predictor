import numpy as np
import collections


# Default: High Card : 1-14
# Pair : 15-29
# Two Pair : 30-44
# Three of a Kind : 45-59
# Straight : 60-74
# Flush : 75-89
# Full House : 90-104
# Four of kind : 105-119
# Straight Flush : 120-134
# Royal Straight Flush : 135


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


def score_for_royal_flush(numbers):
    numbers.sort()
    np.asarray(numbers)
    if (np.sum(np.diff(numbers)) == 4) and (numbers[0] + numbers[4] == 24):
        return 135
    return 0


def score_for_straight(numbers):
    numbers.sort()
    numbers = np.asarray(numbers)
    if np.sum(np.asarray(np.diff(numbers))) == 4:
        return numbers[-1]
    return 0


def score_for_four_of_a_kind(numbers):
    score = 105
    freq = collections.Counter(numbers)
    for key in freq.keys():
        if freq[key] == 4: return score + key
    return 0


def score_for_full_house(numbers):
    freq = collections.Counter(numbers)
    for key in freq.keys():
        if freq[key] == 3:
            return 90 + key
    return 0


def score_for_three_of_a_kind(numbers):
    freq = collections.Counter(numbers)
    if 3 in freq.values():
        for key in freq.keys():
            if freq[key] == 3:
                return 45 + key
    return 0


def score_for_two_pairs(numbers):
    freq = collections.Counter(numbers)
    score = 30
    l1 = list(freq.values())
    l1.sort(reverse=True)
    if l1 == [2, 2, 1]:
        vals = []
        for val in freq.keys():
            if freq[val] == 2:
                vals.append(val)
            elif freq[val] == 1:
                score += val / 10000
        vals.sort(reverse=True)
        score += vals[0] + (vals[1] / 100)
        return score
    return 0


def score_for_one_pair(numbers):
    freq = collections.Counter(numbers)
    l1 = list(freq.values())
    l1.sort(reverse=True)
    if l1 == [2, 1, 1, 1]:
        score = 15
        vals = []
        for key in freq.keys():
            if freq[key] == 2:
                score += key
            elif freq[key] == 1:
                vals.append(key)
        vals.sort(reverse=True)
        for i, val in enumerate(vals):
            score += val / pow(10, 2 * (1 + i))
        return score
    return 0


def score_for_high_card(numbers):
    numbers.sort(reverse=True)
    score = numbers[0]
    for i in range(1, 5):
        score += (numbers[i]) / (pow(10, 2 * i))
    return score


def winner_pred_wrapper(sample_hand):
    score = []

    for hand in sample_hand:
        ## Data Pre-processing
        base_numbers = helper_get_numbers(hand)
        base_suit = helper_get_suit_list(hand)
        freq = collections.Counter(base_numbers)
        freq_count = list(freq.values())
        freq_count.sort(reverse=True)

        str = ''
        for s in base_suit:
            str += s
        ref_str = str[0] * len(str)

        if freq_count == [1, 1, 1, 1, 1]:
            if str == ref_str:
                tmp1 = score_for_royal_flush(base_numbers)
                if not tmp1:
                    tmp2 = score_for_straight(
                        base_numbers)  # Checked above for same suit, same suit + straight = straight flush
                    if not tmp2:
                        score.append(score_for_high_card(base_numbers) + 75)  # '+75' because effectively flush
                    elif tmp2:
                        score.append(tmp2 + 120)
                elif tmp1:
                    score.append(tmp1)

            elif str != ref_str:
                tmp2 = score_for_straight(base_numbers)
                if tmp2:
                    score.append(tmp2 + 60)  # Not same suit but straight = Just straight
                else:
                    score.append(score_for_high_card(base_numbers))

        elif freq_count[0] == 4:
            score.append(score_for_four_of_a_kind(base_numbers))

        elif freq_count[0] == 3:
            if len(freq_count) == 2:
                score.append(score_for_full_house(base_numbers))
            elif len(freq_count) == 3:
                score.append(score_for_three_of_a_kind(base_numbers))

        elif freq_count[0] == 2:
            if len(freq_count) == 3:
                score.append(score_for_two_pairs(base_numbers))
            elif len(freq_count) == 4:
                score.append(score_for_one_pair(base_numbers))

    return score

## Main

## Sample test for royal flush
# sample_hand0 = [['C10', 'C11', 'C12', 'C14', 'C13']]
# print(winner_pred_wrapper(sample_hand0))

## Sample test for straight flush
# sample_hand1 = ['C5', 'C6', 'C7', 'C8', 'C4']
# sample_hand2 = ['D4', 'D5', 'D6', 'D7', 'D8']
# print(winner_pred_wrapper([sample_hand1, sample_hand2]))


# Sample test for 4 of a kind
# sample_hand3 = ['C8', 'D8', 'S8', 'H8', 'C12']
# sample_hand4 = ['D5', 'D3', 'C5', 'H5', 'S5']
# print(winner_pred_wrapper([sample_hand3, sample_hand4]))

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
# sample_hand10 = ['H12', 'S12', 'C8', 'C9', 'C12']
# print(winner_pred_wrapper([sample_hand9, sample_hand10]))


## Sample test for Two pair
# sample_hand11 = ['S9', 'H9', 'C4', 'H7', 'S7']
# sample_hand12 = ['S9', 'H9', 'C8', 'H7', 'S7']
# print(check_for_two_pairs(sample_hand11))
# print(check_for_two_pairs(sample_hand12))


## Sample test for One pair
# sample_hand12 = ['S9', 'H9', 'S8', 'S5', 'S4']
# sample_hand13 = ['D9', 'C9', 'D8', 'D5', 'D3']
# print(winner_pred_wrapper(sample_hand12))
# print(winner_pred_wrapper(sample_hand13))


## Sample test for High Card
# sample_hand14 = ['S9', 'S12', 'S14', 'S6', 'C5']
# sample_hand15 = ['C9', 'C12', 'C14', 'C6', 'S5']
# print(winner_pred_wrapper([sample_hand14, sample_hand15]))

# a = ['S13', 'S11', 'S9', 'S10', 'S12']
# b = ['C5', 'D6', 'D3', 'D4', 'C2']
# print(winner_pred_wrapper([a, b]))


# a = ['S9', 'C9', 'S9', 'H3', 'C3']
# b = ['H2', 'C2', 'S2', 'D2', 'H14']
# print(winner_pred_wrapper([a, b]))
