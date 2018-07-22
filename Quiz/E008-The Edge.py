"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    items = float(input()), float(input()), float(input()), float(input()), float(input())

    print('Total: %.2f THB' % sum(items))
    print('Maximum: %.2f THB' % max(items))
    print('Minimum: %.2f THB' % min(items))
    print('Average: %.2f THB' % (sum(items)/5))

main()
