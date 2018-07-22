"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    data = {'Quick': (0.8, 0.96, 1.12), 'Arts': (1, 1.2, 1.4), 'Buster': (1.5, 1.8, 2.1)}
    base_dmg, total_dmg = int(input()), 0
    card = [input(), input(), input()]

    for i in range(len(card)):
        total_dmg += base_dmg*data[card[i]][i]

    if card[0] == 'Buster':
        total_dmg *= 1.5

    if card.count('Buster') == 3:
        total_dmg += 0.6*base_dmg

    print(int(total_dmg))

main()
