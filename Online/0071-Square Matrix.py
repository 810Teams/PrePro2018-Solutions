"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    matrix = ''
    size = int(input())

    for _ in range(size):
        for _ in range(size):
            matrix += str(int(input())) + ' '
        matrix += '\n'

    print(matrix)

main()
