"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    # Bottle Cap
    print(' '*(num - 1) + '*'*num)

    # Bottle Neck
    print((' '*(num - 1) + '*' + ' '*(num - 2) + '*\n')*num, end='')

    # Bottle Curve
    for i in range(1, num - 1):
        print(' '*(num - 1 - i) + '*' + ' '*(num - 2 + i*2) + '*')

    # Bottle Body
    print(('*' + ' '*(num + (num - 2)*2) + '*\n')*num*2, end='')

    # Bottle Bottom
    print('*'*(num + (num-2)*2 + 2))

main()
