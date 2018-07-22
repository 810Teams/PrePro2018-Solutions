"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import pi

def main():
    """ Main function """
    total = 0
    total += cylinder_vol(float(input()), float(input()))
    total += cylinder_vol(float(input()), float(input()))
    total += cylinder_vol(float(input()), float(input()))
    total += cylinder_vol(float(input()), float(input()))
    total += cylinder_vol(float(input()), float(input()))

    print('Total %.2f ml.' % total)

def cylinder_vol(radius, height):
    """ Calculate volume of cylinder """
    return pi*radius**2*height

main()
