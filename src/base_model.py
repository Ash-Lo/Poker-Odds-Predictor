## Base code to draw simple cards
import random
import Winner_pred
from itertools import combinations


def draw_cards(N ,suit ,value):
    Drawn_Cards = []
    result = {}
    temp_draw = []

    for i in range(1, N+1):
        while len(temp_draw) < 2:
            temp_val = random.choice(value)
            temp_suite = random.choice(suit)
            temp_card = temp_suite + str(temp_val)
            if temp_card not in Drawn_Cards:
                temp_draw.append(temp_card)
                Drawn_Cards.append(temp_card)
        result[i] = temp_draw
        temp_draw = []

    return result, Drawn_Cards


def community_cards(Drawn_Cards, suit, value):

    community_cards = []
    for i in range(3):
        temp_val = random.choice(value)
        temp_suite = random.choice(suit)
        temp_card = temp_suite + str(temp_val)
        if temp_card not in Drawn_Cards:
            community_cards.append(temp_card)

    return community_cards


def build_deck(suit, value):
    deck =[]
    nums = list(value)
    for i in nums:
        for s in suit:
            deck.append(s + str(i))
    return deck


## Main
players = 3
suit = ['D', 'H', 'S', 'C']
value = [i for i in range(2, 15)] #Ace is given value 14
deck = build_deck(suit, value)
Player_Hands, Drawn_Cards = draw_cards(players, suit, value)
Community_cards = community_cards(Drawn_Cards, suit, value)
remaining_cards = []

for card in deck:
    if card not in set(Drawn_Cards):
        remaining_cards.append(card)
#print(len(remaining_cards))
remaining_cards = combinations(remaining_cards, r=3)
hands = []
for combo in remaining_cards:
    hands.append(combo)
#print(len(hands))


# temp = ['H3', 'C3', 'D4', 'H4']
# new = []
# val = combinations(temp, r=3)
# for list in val:
#     for val in list:
#         print(val)
#     new.append(list)
# print(new)