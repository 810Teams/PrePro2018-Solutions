"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import log10

def main():
    """ Main function """
    num = float(input())
    print('%.2f' % (2*log10(num) + num/3))

main()
