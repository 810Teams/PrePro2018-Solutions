"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    print('@ '*(num//2 + 1))
    print('@'*num)
    print(' ' + '@'*(num-2) + ' ')

    for _ in range((num - 7)//2):
        print('  ' + '@ '*(num//2 - 1))
        print('  ' + '@'*(num - 4))

    print('  ' + '@ '*(num//2 - 1))
    print(' ' + '@'*(num-2) + ' ')
    print('@'*num)
    print('@'*num)

main()
