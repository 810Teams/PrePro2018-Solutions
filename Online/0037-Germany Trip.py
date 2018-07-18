"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

import math

def main():
    """ Main function """
    x_1, y_1 = int(input()), int(input())
    x_2, y_2 = int(input()), int(input())
    x_3, y_3 = int(input()), int(input())
    x_4, y_4 = int(input()), int(input())
    x_5, y_5 = int(input()), int(input())

    distance = distance_cal(x_1, y_1, x_2, y_2)
    distance += distance_cal(x_2, y_2, x_3, y_3)
    distance += distance_cal(x_3, y_3, x_4, y_4)
    distance += distance_cal(x_4, y_4, x_5, y_5)

    print(math.ceil(distance))

def distance_cal(x_a, y_a, x_b, y_b):
    """ Calculate distance between 2 points """
    return math.sqrt((x_a - x_b)**2 + (y_a - y_b)**2)

main()
