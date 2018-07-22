"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    size_i, size_j = int(input()), int(input())

    for i in [[int(input()) for _ in range(size_j)] for _ in range(size_i)]:
        for j in i:
            print(j, end=' ')
        print()

main()
