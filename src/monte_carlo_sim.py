import math

from poker import Card
import random
import Winner_pred
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from scipy.stats import norm


def simulate(n_players, own_cards, table_cards, rest_deck):
    if len(table_cards) not in [0, 3, 4, 5]:
        raise Exception("incorrect table cards count")
    if len(own_cards) != 2:
        raise Exception("incorrect own cards count")

    win_ct = 0
    sim_ct = 10000

    for _ in range(sim_ct):
        new_deck = [c for c in rest_deck]
        new_table_cards = [c for c in table_cards]
        random.shuffle(new_deck)
        other_players = []
        for i in range(n_players):
            other_players.append([])
            for _ in range(2):
                other_players[i].append(new_deck.pop())

        while len(new_table_cards) < 5:
            new_table_cards.append(new_deck.pop())

        self_score = 0
        for c1 in range(3):
            for c2 in range(c1 + 1, 4):
                for c3 in range(c2 + 1, 5):
                    cur_hand = own_cards + [new_table_cards[c1], new_table_cards[c2], new_table_cards[c3]]
                    trans_cur_hand = hand_transform(cur_hand)
                    score = Winner_pred.winner_pred_wrapper([trans_cur_hand])[0]
                    if score > self_score:
                        self_score = score

        max_other_score = 0
        for pl in other_players:
            for c1 in range(3):
                for c2 in range(c1 + 1, 4):
                    for c3 in range(c2 + 1, 5):
                        cur_hand = pl + [new_table_cards[c1], new_table_cards[c2], new_table_cards[c3]]
                        trans_cur_hand = hand_transform(cur_hand)
                        score = Winner_pred.winner_pred_wrapper([trans_cur_hand])[0]
                        if score > max_other_score:
                            max_other_score = score

        if self_score > max_other_score:
            win_ct += 1

    return win_ct * 100.0 / sim_ct


def simulate_mle(n_players, own_cards, table_cards, rest_deck):
    if len(table_cards) not in [3, 4, 5]:
        raise Exception("incorrect table cards count")
    if len(own_cards) != 2:
        raise Exception("incorrect own cards count")

    x = []

    for sc in range(100):
        win_ct = 0
        sim_ct = 1000

        for _ in range(sim_ct):
            new_deck = [c for c in rest_deck]
            new_table_cards = [c for c in table_cards]
            random.shuffle(new_deck)
            other_players = []
            for i in range(n_players):
                other_players.append([])
                for _ in range(2):
                    other_players[i].append(new_deck.pop())

            while len(new_table_cards) < 5:
                new_table_cards.append(new_deck.pop())

            self_score = 0
            for c1 in range(3):
                for c2 in range(c1 + 1, 4):
                    for c3 in range(c2 + 1, 5):
                        cur_hand = own_cards + [new_table_cards[c1], new_table_cards[c2], new_table_cards[c3]]
                        trans_cur_hand = hand_transform(cur_hand)
                        score = Winner_pred.winner_pred_wrapper([trans_cur_hand])[0]
                        if score > self_score:
                            self_score = score

            max_other_score = 0
            for pl in other_players:
                for c1 in range(3):
                    for c2 in range(c1 + 1, 4):
                        for c3 in range(c2 + 1, 5):
                            cur_hand = pl + [new_table_cards[c1], new_table_cards[c2], new_table_cards[c3]]
                            trans_cur_hand = hand_transform(cur_hand)
                            score = Winner_pred.winner_pred_wrapper([trans_cur_hand])[0]
                            if score > max_other_score:
                                max_other_score = score

            if self_score > max_other_score:
                win_ct += 1

        x.append(win_ct * 100.0 / sim_ct)

    return x, np.mean(x), math.sqrt(np.var(x))

def hand_transform(hand):
    new_hand = []
    for card in hand:
        rank = card.rank._value_[0]
        if rank.isnumeric():
            rank = int(rank)
        else:
            if rank == "J":
                rank = 11
            elif rank == "Q":
                rank = 12
            elif rank == "K":
                rank = 13
            else:
                rank = 14

        new_hand.append(str(card.suit._value_[1]).upper() + str(rank))
    return new_hand


if __name__ == "__main__":
    deck = list(Card)
    random.shuffle(deck)

    own_cards = [Card([7, "d"]), Card(["Q", "d"])]

    # table_cards = []
    # table_cards = [Card([3, "d"]), Card(["Q", "s"]), Card([9, "d"])]
    # table_cards = [Card([3, "d"]), Card(["Q", "s"]), Card([9, "d"]), Card([2, "c"])]
    table_cards = [Card([3, "d"]), Card(["Q", "s"]), Card([9, "d"]), Card([2, "c"]), Card([5, "d"])]

    for c in own_cards:
        deck.remove(c)

    for c in table_cards:
        deck.remove(c)

    # own_cards = []
    # for _ in range(2):
    #     own_cards.append(deck.pop())

    # table_card_ct = 3
    # table_cards = []
    #
    # for _ in range(table_card_ct):
    #     table_cards.append(deck.pop())

    print(own_cards)
    print(table_cards)

    print(simulate(4, own_cards, table_cards, deck))

    # data, mu, sigma = simulate_mle(4, own_cards, table_cards, deck)
    #
    # print(data)
    #
    # n, bins, patches = plt.hist(data, 20, density = True, facecolor='skyblue', alpha=0.75)
    #
    # # add a 'best fit' line
    # y = norm.pdf(bins, mu, sigma)
    # l = plt.plot(bins, y, 'o--', linewidth=2)
    #
    # plt.xlabel('Win percentage')
    # plt.ylabel('Probability')
    # plt.title(r'$\mathrm{Histogram\ of\ Win\ percentage:}\ \mu=%.3f,\ \sigma=%.3f$' % (mu, sigma))
    # plt.grid(True)
    #
    # plt.show()

    # deck2 = list(Card)
    # random.shuffle(deck2)
    #
    # strong_own_cards = [Card(["K", "d"]), Card(["K", "c"])]
    #
    # for c in strong_own_cards:
    #     deck2.remove(c)
    #
    # for c in table_cards:
    #     deck2.remove(c)
    #
    # probs = []
    # probs_strong = []
    # pl = []
    # for n_pl in range(2, 9):
    #     pl.append(n_pl)
    #     probs.append(simulate(n_pl, own_cards, table_cards, deck))
    #     probs_strong.append(simulate(n_pl, strong_own_cards, table_cards, deck2))
    #
    # plt.plot(pl, probs, label= "Average hand")
    # plt.plot(pl, probs_strong, label = "Strong hand")
    # plt.xlabel('Players')
    # plt.ylabel('Win probability')
    # plt.title('Win probability vs number of players')
    # plt.legend()
    # plt.show()
