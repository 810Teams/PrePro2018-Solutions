"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    combo = 0

    while True:
        word = input()

        # Combo chaining
        if combo == 0 and word == 'Pen':
            combo = 1
        elif combo == 1 and word == 'Pineapple':
            combo = 2
        elif combo == 2 and word == 'Apple':
            combo = 3
        elif combo == 3 and word == 'Pen':
            print('Correct lyrics!')
            break

        # Combo breaks
        elif word == 'Pen':
            combo = 1
            print('Wrong lyrics!')
        else:
            combo = 0
            print('Wrong lyrics!')

main()
