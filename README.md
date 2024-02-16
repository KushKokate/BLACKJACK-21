Blackjack 21 Game

DESCRIPTION:
This Python script simulates a simplified version of the Blackjack card game. The game is played between the user and the computer. The objective of the game is to have a hand value closer to 21 than the dealer without exceeding it.

FEATURES:
Random card dealing.
Calculation of player and dealer scores.
Ability for the user to draw additional cards.
Automatic drawing of cards for the computer based on certain conditions.
Endgame detection and determination of the winner.

HOW TO PLAY:

The game starts by dealing two cards to both the player and the dealer.
The player's current hand and score are displayed, along with the dealer's first card.
The player is prompted to choose whether to draw another card ("yes" or "no").
If the player chooses to draw, another card is added to their hand, and the score is recalculated.
If the player's score exceeds 21, they lose the game.
If the player chooses not to draw or reaches a score of 21, the dealer's turn begins.
The dealer automatically draws cards until their score reaches at least 17.
Once the dealer finishes drawing cards, the final hands and scores are displayed.
The winner is determined based on the scores, and the result is displayed.
Additional Notes:

Aces can be counted as 1 or 11 points, whichever is more beneficial to the player.
Face cards (Jack, Queen, King) are each worth 10 points.
The player wins if their score is closer to 21 than the dealer's score without exceeding 21.
The game detects if either the player or the dealer has a "Blackjack" (an initial hand with a total value of 21) and declares an instant win for that player.
The game provides an option to play again after each round.

REQUIREMENTS:
Python 3.x
random module
replit module (for clearing the console, optional)

ENJOY PLAYING BLACKJACK-21
