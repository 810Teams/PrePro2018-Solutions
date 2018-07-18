"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    for i in range(num-1, -1, -1):
        print(' '*i + '/')

main()
