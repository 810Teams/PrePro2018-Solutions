"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    amount = int(input())
    game, price = list(), list()

    for _ in range(amount):
        data = input().split(' = ')
        game.append(data[0])
        price.append(float(data[1]))

    print('{} is only ${:.2f}!'.format(game[price.index(min(price))], min(price)))

main()
