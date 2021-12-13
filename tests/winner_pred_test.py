import src.Winner_pred

host_hand = ['S10', 'H8']
possible_hand = ['D5', 'C8', 'S2']
print(host_hand)
for x in possible_hand: host_hand.append(x)
print(host_hand)

print(src.Winner_pred.winner_pred_wrapper([host_hand]))