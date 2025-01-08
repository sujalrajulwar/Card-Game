# Card Game

## Overview
This is a simple Python-based card game that simulates a round-based competition between multiple players. Each player is dealt a hand of cards, and they play rounds where a card is randomly selected from their hand. The game continues until all cards are played, and the player who wins the most rounds is declared the overall winner.

## Features
- Shuffle and deal cards to multiple players.
- Play multiple rounds, with each round determining a winner.
- Tracks the score of each player across all rounds.
- Supports any number of players.

## Getting Started

### Prerequisites
- Python 3

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/rushi4git/card-game.git
    cd card-game
    ```

2. Ensure you have Python installed. You can check your Python version using:
    ```bash
    python --version
    ```

### Running the Game
1. Navigate to the project directory.

2. Run the Python script:
    ```bash
    python card_game.py
    ```

3. Follow the on-screen prompts to start the game:
    - Enter the number of players.
    - Play each round by entering the player number who wins the round.

### Example Output
```bash
Enter the number of players: 3

Round 1:
Cards played this round:
Player 1: 7 of Hearts
Player 2: K of Diamonds
Player 3: 3 of Clubs
Enter the player number who wins this round (1, 2, ...): 2

Round 2:
Cards played this round:
Player 1: A of Spades
Player 2: 9 of Clubs
Player 3: 5 of Diamonds
Enter the player number who wins this round (1, 2, ...): 1

...

Game over!
Player 1 wins the game with 5 rounds!
