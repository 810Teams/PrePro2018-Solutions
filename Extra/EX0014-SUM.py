"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    total = 0

    for i in range(1, int(input()) + 1):
        print(' + '.join([str(j) for j in range(1, i + 1)]), '= ', end='')
        print(sum([j for j in range(1, i + 1)]))
        total += sum([j for j in range(1, i + 1)])

    print('SUM:', total)

main()
