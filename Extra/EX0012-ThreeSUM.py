"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    amount = int(input())
    print('Winner is ' + [input(), input(), input()][((1 + amount)*amount)//2%3 - 1] + '!!')

main()
