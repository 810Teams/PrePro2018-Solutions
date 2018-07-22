"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    money, items = 0, 0

    while True:
        action = input()
        if action == 'END':
            break
        action = int(action)

        if action >= 0:
            money += action
        elif money + action >= 0:
            money -= abs(action)
            items += 1
        elif money + action < 0:
            print('ERROR: Not enough money for this item.')

    print('Items:', items)
    print('Change:', money, 'THB')

main()
