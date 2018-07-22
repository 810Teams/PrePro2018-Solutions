"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import ceil

def main():
    """ Main function """
    size, text, mode = int(input()), input(), input()
    text = text[0:size-2]

    print('*'*size)
    print('*%*s*' % (size-2, ''))

    if mode == 'Left':
        print('*%-*s*' % (size-2, text))
    elif mode == 'Right':
        print('*%*s*' % (size-2, text))
    elif mode == 'Center':
        print('*%*s%s%*s*' % (ceil((size-2-len(text))/2), '', text, (size-2-len(text))//2, ''))

    print('*%*s*' % (size-2, ''))
    print('*'*size)

main()
