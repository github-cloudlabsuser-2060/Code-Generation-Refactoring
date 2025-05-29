# Intentionally flawed Python program

"""
This program simulates drawing five cards from a shuffled deck, checks for flush and straight hands,
and calculates the odds of drawing a specific card provided by the user.
"""

# importing modules
import itertools, random

# make a deck of cards as (rank, suit) tuples
# rank: 1-13 (Ace, 2-10, Jack, Queen, King), suit: Spade, Heart, Diamond, Club
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))

# shuffle the cards
random.shuffle(deck)

# draw any number of cards and display them
def display_drawn_cards(deck, num_cards=5):
    """Prints the first num_cards drawn from the deck in a readable format."""
    rank_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    print(f"You got:")
    for i in range(num_cards):
        rank = deck[i][0]
        suit = deck[i][1]
        rank_str = rank_names.get(rank, str(rank))
        print(f"{rank_str} of {suit}")

# check if the drawn cards are a flush (all same suit)
flush = all(card[1] == deck[0][1] for card in deck[:5])
if flush:
    print("You got a flush!")
else:
    print("You did not get a flush.")

# check if the drawn cards are a straight (consecutive values)
rank_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
straight = sorted(card[0] for card in deck[:5])
if straight == list(range(straight[0], straight[0] + 5)):
    straight_str = ', '.join(rank_names.get(rank, str(rank)) for rank in straight)
    print(f"You got a straight! ({straight_str})")
else:
    print("You did not get a straight.")


def calculate_odds_for_specific_card(rank, suit):
    """
    Calculate the odds of drawing a specific card (rank and suit) from a standard 52-card deck.
    Args:
        rank (int): The rank of the card (1-13)
        suit (str): The suit of the card ('Spade', 'Heart', 'Diamond', 'Club')
    Returns:
        float: The probability of drawing the specified card (1/52)
    """
    total_cards = 52
    # Only one card of each rank and suit exists in a standard deck
    odds = 1 / total_cards
    return odds

def main_menu():
    """Main menu for user to choose actions."""
    while True:
        print("\nMain Menu:")
        print("1. Draw cards")
        print("2. Calculate odds for a specific card")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == '1':
            while True:
                try:
                    num_cards = int(input("How many cards would you like to draw? (1-52): "))
                    if 1 <= num_cards <= 52:
                        break
                    else:
                        print("Please enter a number between 1 and 52.")
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            random.shuffle(deck)
            display_drawn_cards(deck, num_cards)
            # Check for flush
            if num_cards >= 5:
                flush = all(card[1] == deck[0][1] for card in deck[:num_cards])
                if flush:
                    print("You got a flush!")
                else:
                    print("You did not get a flush.")
                # Check for straight
                rank_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
                straight = sorted(card[0] for card in deck[:num_cards])
                if straight == list(range(straight[0], straight[0] + num_cards)):
                    straight_str = ', '.join(rank_names.get(rank, str(rank)) for rank in straight)
                    print(f"You got a straight! ({straight_str})")
                else:
                    print("You did not get a straight.")
            else:
                print("Flush and straight checks require at least 5 cards.")
        elif choice == '2':
            user_input = input("Enter the card to calculate odds for (e.g., 'Ace of Spade', '7 of Heart'): ")
            try:
                parts = user_input.strip().split(' of ')
                rank_str, suit = parts[0], parts[1].capitalize()
                rank_map = {'Ace': 1, 'Jack': 11, 'Queen': 12, 'King': 13}
                if rank_str.isdigit():
                    rank = int(rank_str)
                else:
                    rank = rank_map.get(rank_str.capitalize())
                if rank and suit in ['Spade', 'Heart', 'Diamond', 'Club']:
                    odds = calculate_odds_for_specific_card(rank, suit)
                    print(f"Odds of drawing {rank_str} of {suit}: {odds:.2%}")
                else:
                    print("Invalid card input.")
            except Exception:
                print("Invalid input format. Please use the format 'Rank of Suit'.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()


