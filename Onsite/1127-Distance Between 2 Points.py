"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import sqrt

def main():
    """ Main function """
    x_1, y_1 = [int(i) for i in input().strip('()').split(', ')]
    x_2, y_2 = [int(i) for i in input().strip('()').split(', ')]

    print('{:.2f}'.format(sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)))

main()
