# Poker-Odds-Predictor

Introduction - 

We are building an odds probability predictor for the game of Texas Hold’em Poker. This is a mutli-player game in which each player is dealt 2 cards each, and there are 3 common community cards and 2 more cards (Turn card, River card). Concepts of probability are at the heart of poker, since odds change after each card is drawn and the winner at showdown is determined by who has the strongest hand. Based on the knowledge of the cards each player has and community cards, and thus deck cards, we can calculate the odds of winning by calculating the probability based on a priori knowledge. In this project we calculate odds of winning on 2 occasions - 
i. When just the player cards are dealt,
ii. When the community cards are dealt, 
We also determine who won the hand at showdown, based on the cards on the table. This employs determining the strongest hand for each player based on his cards and then using the poker ranking system.

Tentative Plan - 
Build source code files for drawing cards for each player and drawing the community cards.
Determine all the special events as per the rules of the game and calculate the conditional probability of occurrence for each of them.
Calculate the probability of winning for a particular player with the knowledge of his own cards and the table cards, by defining a heuristic. We may also use Monte Carlo simulations to calculate the probability.
Building a module to determine the winner after all players show their cards at the end of the game.

Workload Distribution:
Ashutosh: Part 1 & 2
Rajeev: Part 3 & 4

Tech stack (Tentative):
Python3
Libraries: Numpy, Pandas, Numba, Matplotlib
