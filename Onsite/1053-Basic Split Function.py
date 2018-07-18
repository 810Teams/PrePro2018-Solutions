"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = float(input())

    if num < 0:
        result = num**2
    elif num == 0:
        result = 0
    elif num > 0:
        result = 2*num + 10

    print('%.2f' % result)

main()
