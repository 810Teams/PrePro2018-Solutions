"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    start, stop, step = float(input()), int(input()), float(input())
    counter = 0

    while counter < stop:
        print('%.2f'%(start * step ** counter), end=' ')
        counter += 1

    print()

main()
