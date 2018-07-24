"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    for i in range(num):
        for j in range(num):
            print((i + j + 1), end=' ')
        print()

    for i in range(num):
        for j in range(num):
            print((i + j) % num + 1, end=' ')
        print()

main()
