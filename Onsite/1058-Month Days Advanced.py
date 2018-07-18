"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    month, year = int(input()), int(input())

    if year <= 0 or month <= 0 or month > 12:
        print('Invalid Month or Year')
    elif month in (1, 3, 5, 7, 8, 10, 12):
        print(31)
    elif month in (4, 6, 9, 11):
        print(30)
    elif month == 2:
        if is_leap_year(year):
            print(29)
        else:
            print(28)

def is_leap_year(year):
    """ Check if year is leap year """
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True

    return False

main()
