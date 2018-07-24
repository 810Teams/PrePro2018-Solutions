"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    print(' '*(num-1) + '*' + ' '*((num - 1)*2 - 1) + '*')

    for i in range(0, num-1):
        print(' '*(num-2-i) + '*' + '-'*(i*2 + 1) + '*' + ' '*(num-2-i), end='')
        print(' '*(num-3-i) + '*'*(i < num-2) + '-'*(i*2 + 1) + '*' + ' '*(num-2-i))

    for i in range(1, (num-1)*2+1):
        print(' '*i + '*' + '-'*(num*4 - 5 - i*2) + '*'*(i < (num-1)*2))

main()
