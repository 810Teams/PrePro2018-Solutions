"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import sin, radians

def main():
    """ Main function """
    num = int(input())
    print('%.2f' % (sin(radians(3*num)) + abs(num/4) + 5))

main()
