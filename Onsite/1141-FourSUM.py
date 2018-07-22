"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())
    print('Winner is ' + [input(), input(), input(), input()][((1 + num)*num)//2%4 - 1] + '!!')

main()
