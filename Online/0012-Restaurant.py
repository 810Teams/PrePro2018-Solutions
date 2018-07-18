"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    price = float(input())
    print('Service Charge : %.2f Baht' % (price*0.1))
    print('VAT : %.2f Baht' % (price*0.07))
    print('Total : %.2f Baht' % (price + price*0.1 + price*0.07))

main()
