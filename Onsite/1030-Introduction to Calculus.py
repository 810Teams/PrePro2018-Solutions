"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import sin, cos

def main():
    """ Main function """
    num_a, num_b = int(input()), int(input())
    num_a, num_b = min(num_a, num_b), max(num_a, num_b)

    result = (-3/2)*cos(2*num_b/3) - sin(num_b) + 4*num_b
    result -= (-3/2)*cos(2*num_a/3) - sin(num_a) + 4*num_a

    print('%.2f' % result)

main()
