"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    top = ['', 0, 0, 0] # Game name, price, discounted price, discount percent

    while True:
        data = input()

        if data == 'Enough!!!':
            break

        game, price, discount = data.split(' , ')
        price, discount = float(price.replace(' Baht', '')), float(discount.replace(' %', ''))

        if price*discount*0.01 > top[1]-top[2]:
            top = [game, price, price*(1-discount*0.01), discount]
        elif price*discount*0.01 == top[1]-top[2] and price > top[1]:
            top = [game, price, price*(1-discount*0.01), discount]

    print('Game name:', top[0])
    print('Sale price: {:.2f} Baht'.format(top[2]))
    print('Percentage: {:.2f} %'.format(top[3]))

main()
