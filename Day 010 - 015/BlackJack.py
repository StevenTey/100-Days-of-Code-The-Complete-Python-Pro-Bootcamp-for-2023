'''
Create a BlackJack game in Python
'''

# Import necessary packages
import random

# Create deal card function
def deal_card():
    '''Returns a random card from the deck'''
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

# Create calculate score function
def calculate_score(cards):
    '''Take a list of cards and return the score calculated from the cards'''
    # Check for blackjack (ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check for 11 (ace) and replace with 1 if score > 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # Return sum of cards
    return sum(cards)

# Create compare function
def compare(user_score, computer_score):
    '''Compare user and computer scores and return result'''
    # Check for blackjack
    if user_score == 0 or computer_score == 0:
        if user_score == 0:
            return "You win with a blackjack!"
        else:
            return "You lose, opponent has a blackjack!"
    # Check for score > 21
    elif user_score > 21 or computer_score > 21:
        if user_score > 21:
            return "You went over. You lose!"
        else:
            return "Opponent went over. You win!"
    # Check for highest score
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

# Create play game function
def play_game():
    '''
    Play a game of blackjack vs computer
    '''
    # Deal initial cards
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # Calculate scores
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")
        # Check for blackjack or score > 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        # Ask user if they want to draw another card
        else:
            draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
            if draw_card == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer draws cards if score < 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    # Print final scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    # Compare scores
    print(compare(user_score, computer_score))

# Play game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()