"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from json import loads

def main():
    """ Main function """
    start, stop = loads(input()), loads(input())

    if abs(start[0]-stop[0]) == abs(start[1]-stop[1]):
        print('Yes')
    else:
        print('No')

main()
