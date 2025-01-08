import random

# Define card ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create a deck of cards
deck = [(rank, suit) for rank in ranks for suit in suits]

# Function to deal cards to players
def deal_cards(num_players):
    # Shuffle the deck of cards randomly
    random.shuffle(deck)

    # Create empty hands for each player
    hands = [[] for _ in range(num_players)]

    # Calculate the number of cards each player should receive
    cards_per_player = len(deck) // num_players

    # Distribute cards evenly among players
    for i in range(num_players):
        hands[i] = deck[i * cards_per_player:(i + 1) * cards_per_player]
    return hands

# Function to play a round and determine the winner
def play_round(round_number, hands):
    # Display the current round number
    print(f"\nRound {round_number + 1}:")

    # Create a list to store cards played this round
    round_cards = []

    # Randomly select a card from each player's hand
    for hand in hands:
        if hand:
            # Randomly pop a card from the player's hand
            card = hand.pop(random.randint(0, len(hand) - 1))
            round_cards.append(card)
        else:
            round_cards.append(None)

    # Check if there are any valid cards to be played this round
    if all(card is None for card in round_cards):
        print("No cards left to play this round.")
        return None

    # Display the cards played this round
    print("Cards played this round:")
    for i, card in enumerate(round_cards):
        if card:
            print(f"Player {i + 1}: {card[0]} of {card[1]}")

    while True:
        try:
            # Prompt the user to enter the player number who wins this round
            winner_index = int(input("Enter the player number who wins this round (1, 2, ...): ")) - 1
            if 0 <= winner_index < len(hands) and round_cards[winner_index] is not None:
                break
            else:
                print("Invalid player number or player has no cards left. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid player number.")
    #print(card)
    return winner_index

# Main game function
def play_game():
    num_players = 0
    while num_players <= 0:
        try:
            # Prompt the user to enter the number of players
            num_players = int(input("Enter the number of players: "))
            if num_players <= 0:
                print("Please enter a positive number of players.")
        except ValueError:
            print("Invalid input. Please enter a positive number of players.")

    # Deal cards to the players
    hands = deal_cards(num_players)

    # Create a list to store the scores of each player
    player_scores = [0] * num_players

    # Limit rounds to the number of cards in the deck
    num_rounds = min(len(hands[0]), 52)

    # Play each round
    for round_number in range(num_rounds):
        winner_index = play_round(round_number, hands)
        if winner_index is not None:
            player_scores[winner_index] += 1

    # Determine the overall winner
    overall_winner = player_scores.index(max(player_scores)) + 1

    # Display the game result
    print("\nGame over!")
    print(f"Player {overall_winner} wins the game with {max(player_scores)} rounds!")

# Run the game
play_game()
