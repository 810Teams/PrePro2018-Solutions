"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    data = list()
    sec = int(input())

    mins = sec//60
    sec %= 60
    data.insert(0, ['Second', sec])

    hrs = mins//60
    mins %= 60
    data.insert(0, ['Minute', mins])

    days = hrs//24
    hrs %= 24
    data.insert(0, ['Hour', hrs])

    months = days//30
    days %= 30
    data.insert(0, ['Day', days])

    years = months//12
    months %= 12
    data.insert(0, ['Month', months])
    data.insert(0, ['Year', years])

    for i in data:
        print('{}{}'.format(i[1], i[0]) + 's'*(i[1] > 1), end=' ')
    print()

main()
