"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    for i in range(1, num+1):
        print(' ' * (num-i), end='')
        print('*' * i)

main()
