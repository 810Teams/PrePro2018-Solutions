"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    amount, extra, demand, price = int(input()), int(input()), int(input()), int(input())

    pack = amount + extra

    # Case: Didn't reach promotion point
    if demand % pack < amount:
        get = demand
        pay = ((demand//pack)*amount + (demand % pack)) * price

    # Case: Reaches the promotion point
    else:
        get = (demand//pack)*pack + pack
        pay = (((demand//pack)*pack + pack)//pack*amount) * price

    print('Pay:', pay)
    print('Get:', get)

main()
