import random

# function to find the index of the pile with maximum matches
def find_max_pile(piles):
    max_pile_index = 0
    max_matches = piles[max_pile_index]
    for i in range(1, len(piles)):
        if piles[i] > max_matches:
            max_pile_index = i
            max_matches = piles[max_pile_index]
    return max_pile_index

# function to play a single turn of the game
def play_turn(piles):
    pile_index = find_max_pile(piles)
    max_matches = min(piles[pile_index], 3)
    num_matches = random.randint(1, max_matches)
    piles[pile_index] -= num_matches
    return pile_index, num_matches

# function to check if the game is over
def game_over(piles):
    return sum(piles) == 0

# main function to play the game
def play_game(num_piles):
    piles = [random.randint(1, 1000) for _ in range(num_piles)]
    player = 1
    while not game_over(piles):
        print(f"Piles: {piles}")
        pile_index, num_matches = play_turn(piles)
        print(f"Player {player} takes {num_matches} matches from pile {chr(pile_index + ord('A'))}")
        player = 3 - player  # switch to the other player
    print(f"Player {player} wins!")
