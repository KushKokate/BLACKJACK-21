import random
from replit import clear

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def play_game():
    user_card = []
    computer_card = []

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare_score(user_score, computer_score):
        if user_score == compare_score:
            return "DRAw"
        elif compare_score == 0:
            return "Lose opponent has blackjack"
        elif user_score == 0:
            return "won you have blackjack"
        elif computer_score > 21:
            return "you won Opponent went overhead"
        elif user_score > 21:
            return "You lost , you went overhead"
        elif user_score > computer_score:
            return "You Won"
        else:
            return "you lost :{"

    is_game_over = False  
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"your card {user_card} and your score {user_score}")
        print(f"computer's first card {computer_card[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        user_should_deal = input("do you wanna draw a card type 'yes' or else 'no': ")
        if user_should_deal == "yes":
            user_card.append(deal_card())
        else:
            is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)

    print(f"your hand {user_card} and you score {user_score}")
    print(f"computer's hand {computer_card} and score {computer_score}")
    print(compare_score(user_score, computer_score))

play_game()
while input("Do you wanna play again 'y' or 'no'") == "y":
    clear()
    play_game()
