"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    money, cap = int(input()), int(input())
    notes = 0

    notes += money//1000
    money %= 1000
    notes += money//500
    money %= 500
    notes += money//100
    money %= 100
    notes += money//50
    money %= 50
    notes += money//20

    if notes > cap:
        print('No')
    else:
        print('Yes')

main()
