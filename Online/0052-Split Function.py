"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import sin, radians, sqrt, log10

def main():
    """ Main function """
    num = float(input())

    if num < 100:
        result = 2 * sin(radians(num-10))
    elif num == 100:
        result = sqrt(num)/5
    elif num > 100:
        result = log10(num)

    print('%.2f' % result)

main()
