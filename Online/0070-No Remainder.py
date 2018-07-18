"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num, div = int(input()), int(input())

    if num > 0:
        for i in range(num, 0, -1):
            if i % div == 0:
                print(i)

    elif num < 0:
        for i in range(num, 0, 1):
            if i % div == 0:
                print(i)

main()
