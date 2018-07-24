"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num, rounder = int(input()), int(input())
    print(num//(10**rounder)*(10**rounder))

main()
