"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    coor_x, coor_y = int(input()), int(input())

    if coor_x == 0 and coor_y > 0:
        print('North')
    elif coor_x > 0 and coor_y == 0:
        print('East')
    elif coor_x == 0 and coor_y < 0:
        print('South')
    elif coor_x < 0 and coor_y == 0:
        print('West')
    elif coor_x > 0 and coor_y > 0:
        print('Northeast')
    elif coor_x > 0 and coor_y < 0:
        print('Southeast')
    elif coor_x < 0 and coor_y < 0:
        print('Southwest')
    elif coor_x < 0 and coor_y > 0:
        print('Northwest')
    else:
        print('Origin')

main()
