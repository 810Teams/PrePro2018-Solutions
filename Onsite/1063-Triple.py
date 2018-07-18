"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())
    value = 1
    counter = 0

    while counter < num:
        print(value)
        value *= 3
        counter += 1

main()
