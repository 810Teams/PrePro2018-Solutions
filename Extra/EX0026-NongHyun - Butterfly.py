"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    alpha, size = input(), int(input())

    for i in range(1, size//2 + 1):
        print(alpha*i + ' '*(size - 2*i) + alpha*i)

    for i in range(size//2 - 1, 0, -1):
        print(alpha*i + ' '*(size - 2*i) + alpha*i)

main()
