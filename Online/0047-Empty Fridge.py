"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    cola, tea, orange = int(input()), int(input()), int(input())
    strawberry, milk = int(input()), int(input())

    print('-Shopping List-')

    if cola < 12:
        print('Cola x%i' % (12-cola))
    if tea < 16:
        print('Tea x%i' % (16-tea))
    if orange < 20:
        print('Orange Juice x%i' % (20-orange))
    if strawberry < 24:
        print('Strawberry Juice x%i' % (24-strawberry))
    if milk < 32:
        print('Milk x%i' % (32-milk))

main()
