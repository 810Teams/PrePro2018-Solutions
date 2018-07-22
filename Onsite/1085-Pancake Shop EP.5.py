"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    price = float(input())

    print('|' + '-' * 8 + '|')
    print('|%-8.2f|' % price)
    print('|' + '-' * 8 + '|')
    print()
    print('|' + '-' * 8 + '|')
    print('|%8.2f|' % price)
    print('|' + '-' * 8 + '|')
    print()
    print('|' + '-' * 8 + '|')
    print('|%08.2f|' % price)
    print('|' + '-' * 8 + '|')

main()
