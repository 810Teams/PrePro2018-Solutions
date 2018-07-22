"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    price = int(input()) + int(input())

    print('Total: %.2f THB' % price)
    print('Service: %.2f THB' % (price*0.09))
    print('VAT: %.2f THB' % (price*1.09*0.075))
    print('Final Price: %.2f THB' % (price*1.09*1.075))

main()
