"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    _ = [print(i) for i in sorted([int(input()) for i in range(int(input()))], reverse=True)]

main()
