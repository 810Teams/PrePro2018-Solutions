"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    total = 0
    total += promotion(int(input()), int(input()))
    total += promotion(int(input()), int(input()))
    total += promotion(int(input()), int(input()))
    total += promotion(int(input()), int(input()))
    print('%.2f' % total)

def promotion(price_a, price_b):
    """ Dog food promotion """
    return (price_a + price_b) * 0.85

main()
