"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    money = int(input())

    print(money//1000)
    money %= 1000

    print(money//500)
    money %= 500

    print(money//100)
    money %= 100

    print(money//50)
    money %= 50

    print(money//20)
    money %= 20

    print(money//10)

main()
