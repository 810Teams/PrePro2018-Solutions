"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num, index = str(abs(int(input()))), int(input())

    if index <= 0:
        print('Index error.')
    elif index > len(num):
        print('Index out of range.')
    else:
        print(num[-index])

main()
