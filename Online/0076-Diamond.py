"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(int(input())//2) + 1

    for i in range(1, num+1):
        print(' ' * (num-i) + '*' * (i*2-1))

    for i in range(num-1, 0, -1):
        print(' ' * (num-i) + '*' * (i*2-1))

main()
