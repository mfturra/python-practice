import random

# available card options
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw_one_card(user):
    '''Randomly assigns a card to the user requesting one additional card'''
    user.append(random.choice(cards))

# evaluate the sum of the users_cards
def check_player_score(p1_cards, p2_cards):
    '''Checks the current cards of both players and outputs their current total score'''
    # evaluate the sum of player 1's cards
    users_score = sum(users_cards)

    # output the cards player 1 has along with their current total score
    print(f"\nYour cards: {users_cards}, current score: {users_score}")
    print(f"Dealer's first card: {p2_cards[0]}")

    return users_score

# create empty list for users_cards & dealers_cards
users_cards = []
dealers_cards = []

# append new values to users_cards based on available cards in list
draw_one_card(users_cards)
draw_one_card(users_cards)

draw_one_card(dealers_cards)
draw_one_card(dealers_cards)
dealers_score = sum(dealers_cards)

# output current user and dealer card totals
users_score = check_player_score(users_cards, dealers_cards) 

# check if player's score is over 21
while users_score <= 21:
    # if user has less than 21, they can ask for more cards
    user_card_req = input(f"Type 'y' to get another card, type 'n' to pass: ")

    print(f"This is the users card request: {user_card_req}")
    # if user wants a new card, give them a card and output their total score along with the dealers total score
    if user_card_req == 'y':
        # draw another card and evaluate the current score 
        draw_one_card(users_cards)

        # calc users current score
        users_score = sum(users_cards)

        if users_score > 21:
            print(f"\nYour final hand: {users_cards}, final score: {users_score}")

            # track dealers card pick ups
            while dealers_score <= 20:

                # create dealer_final_pickup func
                draw_one_card(dealers_cards)
                dealers_score = sum(dealers_cards)
                print(f"Dealers current cards are: {dealers_cards}")
        else:
            print(f"\nYour cards: {users_cards}, current score: {users_score}")
            print(f"Dealer's first card: {dealers_cards[0]}\n")
                    
    elif user_card_req == 'n':
        # more_cards = False
        print(f'Dealers turn to show their cards: {dealers_cards}')
        # return f"Do you want to play a game of Blackjack Type 'y' or 'n': "
    
# def evaluate_winner(p1_cards, p2_cards):
#             '''Check to see whether either players current cards are over 21'''
#             users_score = sum(p1_cards)

#             # check if user went over 21
#             if users_score > 21:
#                 # when user goes over 21, they automatically lose
#                 print("You went over! The dealer won.")
#             else:
#                 # cycle through dealers card choices until a winner is found
#                 if dealers_cards >= 21: