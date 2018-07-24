"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    for i in range(1, num + 1):
        for j in range(1, num + 1):
            if i == j == num//2 + 1:
                print('#', end='')
            elif j == num//2 + 1:
                print('|', end='')
            elif (i + j) % 2 == 0:
                print('+', end='')
            elif (i + j) % 2 == 1:
                print('-', end='')
        print()

main()
