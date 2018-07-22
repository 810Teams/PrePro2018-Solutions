"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    numlist = [int(input()) for _ in range(int(input()))]
    target = int(input())
    print(target, 'is at index', numlist.index(target))

main()
