"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

import math as m

def main():
    """ Main function """
    var_x, var_a = float(input()), float(input())

    var_y = var_x * m.cos(m.radians(var_a))
    var_y -= m.sqrt(var_a**3 + m.sqrt(var_a*m.sin(m.radians(60)) + m.sqrt(var_a)))
    var_y = abs(int(var_y)) * -1

    print(var_y)

main()
