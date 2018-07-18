"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import pi, sin, radians, sqrt

def main():
    """ Main function """
    num = float(input())

    if num <= 0:
        result = abs(num)**(-1/2*num)
    elif 0 < num <= 2:
        result = 12 * pi * num
    elif num > 2:
        result = (2**num*sin(radians(num)) + sqrt(num))/2

    print('%.2f' % result)

main()
