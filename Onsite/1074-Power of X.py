"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    for i in range(1, num+1):
        for j in range(1, num+1):
            if i == j:
                print('\\', end='')
            elif i + j == num + 1:
                print('/', end='')
            else:
                print(' ', end='')
        print()

main()
