"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    total = 0

    for _ in range(int(input())):
        total += float(input())

    print('%.4f' % total)

main()
