"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    for i in range(int(input())):
        num = int(input())

        if i == 0:
            highest, lowest = num, num

        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num

    print(highest-lowest)

main()
