"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    month = int(input())

    if month in (1, 3, 5, 7, 8, 10, 12):
        print(31)
    elif month in (4, 6, 9, 11):
        print(30)
    elif month in (2,):
        print(28)
    else:
        print('Invalid Month')

main()
