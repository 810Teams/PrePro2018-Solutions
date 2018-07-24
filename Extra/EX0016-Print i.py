"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    mode = end_type(input())
    start, end = int(input()), int(input())

    if start <= end:
        for i in range(start, end+1):
            print('{:02d}'.format(i), end=mode)
    else:
        for i in range(start, end-1, -1):
            print('{:02d}'.format(i), end=mode)

    print()

def end_type(mode):
    """ End """
    if mode == 'Horizontal':
        return ' '
    elif mode == 'Vertical':
        return '\n'

main()
