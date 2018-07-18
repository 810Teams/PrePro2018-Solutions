"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

import math

def main():
    """ Main function """
    velo, deg = int(input()), int(input())

    time = (2*velo*math.sin(math.radians(deg)))/9.8
    height = (velo**2 * math.sin(math.radians(deg))**2)/(9.8*2)
    distance = (velo**2 * math.sin(math.radians(2*deg)))/9.8

    print("t = %.2f" % time)
    print("H = %.2f" % height)
    print("R = %.2f" % distance)

main()
