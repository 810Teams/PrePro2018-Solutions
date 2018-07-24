"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    deg = int(input()) % 360

    if deg == 0 or deg == 180:
        print('x-axis')
    elif deg == 90 or deg == 270:
        print('y-axis')
    elif deg in range(1, 90):
        print(1)
    elif deg in range(91, 180):
        print(2)
    elif deg in range(181, 270):
        print(3)
    elif deg in range(271, 360):
        print(4)

main()
