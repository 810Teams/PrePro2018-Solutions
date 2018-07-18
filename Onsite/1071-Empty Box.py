"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    print('* '*num)
    print(('* ' + '  '*(num - 2) + '*\n')*(num - 2), end='')
    print('* '*num*(num > 1) + '\n'*(num > 1), end='')

main()
