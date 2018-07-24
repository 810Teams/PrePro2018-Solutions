"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    target = int(input())
    cockles = 0
    pot_good = 0
    pot_bad = 0

    while cockles < target:
        amount = int(input())
        time = float(input())
        cleanness = float(input())
        freshness = input()

        if not 28 <= time <= 62:
            pot_bad += 1
            continue

        if cleanness < 90:
            pot_bad += 1
            continue

        if freshness != 'Fresh':
            pot_bad += 1
            continue

        pot_good += 1
        cockles += amount

    print('Cockle: {}'.format(cockles))
    print('Number of good quality: {}'.format(pot_good))
    print('Number of bad quality: {}'.format(pot_bad))

main()
