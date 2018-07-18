"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    # Input 5 Integers
    num_a = int(input())
    num_b = int(input())
    num_c = int(input())
    num_d = int(input())
    num_e = int(input())

    # Calculate 5 y-values from 5 x-values, then show outputs.
    print('%.2f' % parabola(num_a))
    print('%.2f' % parabola(num_b))
    print('%.2f' % parabola(num_c))
    print('%.2f' % parabola(num_d))
    print('%.2f' % parabola(num_e))

def parabola(num):
    """ Parabola equation """
    return (1/25)*num**2 - (6/5)*num + 9

main()
