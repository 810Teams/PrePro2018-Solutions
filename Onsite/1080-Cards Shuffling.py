"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    deck_size = int(input())
    last_card, combo, streak = 0, 0, True

    for _ in range(deck_size):
        card = int(input())
        if card > last_card and streak:
            last_card = card
            combo += 1
        else:
            streak = False

    print(deck_size - combo)

main()
