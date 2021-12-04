import itertools

import numpy as np

import Winner_pred
import base_model
import random
from copy import deepcopy
from itertools import combinations
import numpy


def draw_hands_with_constraints(drawn_cards: dict, num_players, suit, value):
    res= {}
    for i in range(num_players):
        temp_draw = []
        while len(temp_draw) < 2:
            card = random.choice(suit) + str(random.choice(value))
            if card not in drawn_cards.keys():
                temp_draw.append(card)
                drawn_cards[card] = 1
        res[i] = temp_draw
    return res, drawn_cards


def calculate_score(hand_combinations: list):
    res = []
    for i,hand in enumerate(hand_combinations):
        res.append(Winner_pred.winner_pred_wrapper(hand))
    return max(max(res))


def simulate(num_sims=5, num_players=4):
    suit = ['D', 'H', 'S', 'C']
    value = [i for i in range(2, 15)]  # Ace is given value 14

    deck = base_model.build_deck(suit, value)
    draw_cards = {}
    host_hand, drawn_cards_base = draw_hands_with_constraints(draw_cards, 1, suit, value) #Host cards remain same across simulation
    wins, ties = 0, 0
    for i in range(num_sims):
        drawn_cards = deepcopy(drawn_cards_base) #Making sure at the start of each sim, host cards dont change
        player_hands, drawn_cards = draw_hands_with_constraints(drawn_cards, num_players-1, suit, value)
        remaining_deck = base_model.remaining_deck(drawn_cards, deck)
        community_combinations = list(itertools.combinations(remaining_deck, 5))
        community_cards = random.choice(community_combinations)

        host_hand_combinations = base_model.hands_generation(host_hand[0], community_cards)
        host_score = max(Winner_pred.winner_pred_wrapper(host_hand_combinations))

        opponent_score = 0
        for val in player_hands.values():
            hand_combos = base_model.hands_generation(val, community_cards)
            temp = max(Winner_pred.winner_pred_wrapper(hand_combos))
            opponent_score = max(temp, opponent_score)
        #print(host_score, opponent_score)
        if host_score > opponent_score:
            wins += 1

        elif host_score == opponent_score:
            ties += 1
    return wins/num_sims, ties/num_sims
        #print(Winner_pred.winner_pred_wrapper(host_hand_combinations), max(Winner_pred.winner_pred_wrapper(host_hand_combinations)))


## Main
win_prob, tie_prob = simulate(num_sims=50)
print(win_prob, tie_prob)