## Base code to draw simple cards
import random


def draw_cards(N ,suit ,value):
    Drawn_Cards = []
    result = {}
    temp_draw = []

    for i in range(1, N+1):
        while len(temp_draw) <2:
            temp_val = random.choice(value)
            temp_suite = random.choice(suit)
            temp_card = [temp_suite, temp_val]
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
        temp_card = [temp_suite, temp_val]
        if temp_card not in Drawn_Cards:
            community_cards.append(temp_card)

    return community_cards


## Main
players = 3
suit = ['D', 'H', 'S', 'C']
value = [i for i in range(1, 14)]
Player_Hands, Drawn_Cards = draw_cards(players, suit, value)
Community_cards = community_cards(Drawn_Cards,suit,value)
print(Player_Hands)
print(Community_cards)
