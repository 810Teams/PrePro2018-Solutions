"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    amount, price = int(input()), int(input())

    if amount > 15:
        price -= (price % 10)
    elif amount > 10:
        price -= 5

    if price > 300:
        price -= 20
    elif price > 150:
        price -= 10
    else:
        price -= 1

    if 1000 - price >= 0:
        print(1000 - price)
    else:
        print('Not enough money')

main()
