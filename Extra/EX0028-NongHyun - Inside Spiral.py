"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    height, width = int(input()), int(input())

    if height <= width:
        walk = height*2 - 1
    else:
        walk = width*2

    print(walk - 1)

main()
