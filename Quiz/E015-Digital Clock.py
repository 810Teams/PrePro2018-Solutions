"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    alpha = input()

    for i in range(ord('A'), ord('Z') + 1):
        if chr(i) <= alpha:
            print(chr(i), end='')
        else:
            break

    for i in range(ord('a'), ord('z') + 1):
        if chr(i) <= alpha:
            print(chr(i), end='')
        else:
            break

    print()

main()
