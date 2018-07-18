"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    answer = float(input())

    while True:
        num = float(input())
        if num < answer:
            print('More!')
        elif num > answer:
            print('Too Much!')
        else:
            print('Yeah!')
            break

main()
