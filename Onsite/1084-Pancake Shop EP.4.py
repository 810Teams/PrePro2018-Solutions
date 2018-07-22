"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    price = int(input())

    print('|' + '-' * 6 + '|')
    print('|%-6i|' % price)
    print('|' + '-' * 6 + '|')
    print()
    print('|' + '-' * 6 + '|')
    print('|%6i|' % price)
    print('|' + '-' * 6 + '|')
    print()
    print('|' + '-' * 6 + '|')
    print('|%06i|' % price)
    print('|' + '-' * 6 + '|')

main()
