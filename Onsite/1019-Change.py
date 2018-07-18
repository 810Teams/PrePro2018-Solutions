"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    money = int(input())-int(input())

    print(money//100)
    money %= 100

    print(money//50)
    money %= 50

    print(money//20)
    money %= 20

    print(money//10)
    money %= 10

    print(money//5)
    money %= 5

    print(money//2)
    money %= 2

    print(money)

main()
