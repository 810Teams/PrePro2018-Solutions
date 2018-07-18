"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

import math

def main():
    """ Main function """
    radius = float(input())/2

    print("A = %.3f" % (4 * math.pi * radius**2))
    print("V = %.3f" % (4/3 * math.pi * radius**3))

main()
