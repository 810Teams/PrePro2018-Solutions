"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    year = int(input())

    if year <= 0:
        print('This year does not exist.')
    elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, 'is leap year.')
    else:
        print(year, 'is not leap year.')

main()
