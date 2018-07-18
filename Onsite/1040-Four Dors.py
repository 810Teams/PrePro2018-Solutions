"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    a_x, a_y = int(input()), int(input())
    b_x, b_y = int(input()), int(input())
    c_x, c_y = int(input()), int(input())
    d_x, d_y = int(input()), int(input())

    perimeter = 0
    perimeter += calculate(a_x, a_y, b_x, b_y)
    perimeter += calculate(b_x, b_y, c_x, c_y)
    perimeter += calculate(c_x, c_y, d_x, d_y)
    perimeter += calculate(d_x, d_y, a_x, a_y)

    print('%.2f' % perimeter)

def calculate(a_x, a_y, b_x, b_y):
    """ Calculate distance between 2 points """
    return ((a_x - b_x)**2 + (a_y - b_y)**2)**(1/2)

main()
