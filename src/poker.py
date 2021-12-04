import Winner_pred
import base_model

from itertools import combinations


def simulate(num_sims=10, num_players=4):
    suit = ['D', 'H', 'S', 'C']
    value = [i for i in range(2, 15)]  # Ace is given value 14

    player_hands, drawn_cards = base_model.draw_cards(num_players, suit, value)
    deck = base_model.build_deck(suit, value)
    #remaining_deck =


## Main
simulate()