"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    price = float(input())

    print('Price\t%.2f THB' % price)
    print('Service\t%.2f THB' % (price*0.1))
    print('VAT\t%.2f THB' % (price*1.1*0.08))
    print('Total\t%.2f THB' % (price*1.1*1.08))

main()
