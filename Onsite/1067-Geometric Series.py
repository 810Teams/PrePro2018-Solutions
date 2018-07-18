"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    start, stop, step = float(input()), int(input()), float(input())
    counter = 0
    total = 0

    while counter < stop:
        total += (start * step ** counter)
        counter += 1

    print('%.2f' % total)

main()
