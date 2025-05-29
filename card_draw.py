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

def blackjack_count(cards):
    """
    Returns the blackjack card count (Hi-Lo system) for a list of card values.
    2-6: +1, 7-9: 0, 10/J/Q/K/A: -1
    Args:
        cards (list of int): List of card values (1-13, where 1 is Ace, 11-13 are J/Q/K)
    Returns:
        int: The running count
    """
    count = 0
    for card in cards:
        if 2 <= card <= 6:
            count += 1
        elif 7 <= card <= 9:
            count += 0
        elif card == 1 or 10 <= card <= 13:
            count -= 1
    return count

def main_menu():
    """Main menu for user to choose actions."""
    while True:
        print("\nMain Menu:")
        print("1. Draw cards")
        print("2. Calculate odds for a specific card")
        print("3. Blackjack card count (Hi-Lo)")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
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
            print("Enter card values separated by spaces (Ace=1, J=11, Q=12, K=13):")
            user_input = input("Cards: ")
            try:
                card_strs = user_input.strip().split()
                cards = []
                for s in card_strs:
                    s = s.capitalize()
                    if s == 'A' or s == 'Ace':
                        cards.append(1)
                    elif s == 'J' or s == 'Jack':
                        cards.append(11)
                    elif s == 'Q' or s == 'Queen':
                        cards.append(12)
                    elif s == 'K' or s == 'King':
                        cards.append(13)
                    elif s.isdigit() and 2 <= int(s) <= 10:
                        cards.append(int(s))
                    else:
                        raise ValueError(f"Invalid card: {s}")
                count = blackjack_count(cards)
                print(f"Blackjack Hi-Lo count: {count}")
            except Exception as e:
                print(f"Error: {e}\nPlease enter valid card values (e.g., 'A 2 3 10 J Q K').")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()


