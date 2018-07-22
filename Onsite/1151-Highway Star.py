"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import ceil

def main():
    """ Main function """
    dis_a, speed_a = float(input()), float(input())*1000/3600
    dis_b, speed_b = float(input()), 60*1000/3600

    if dis_a/speed_a > (dis_a + dis_b)/speed_b:
        print('Just a bit further away. . .')
    else:
        print('Gureto desu yo')
        print('DO' + 'RA'*max(1, ceil(dis_a/speed_a)))

main()
