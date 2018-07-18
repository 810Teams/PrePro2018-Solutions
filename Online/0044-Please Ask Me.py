"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    number = int(input())

    if number >= 8:
        print('Extremely Happy')
    elif number >= 4:
        print('Very Happy')
    elif number >= 1:
        print('Happy')
    else:
        print('Sad')

main()
