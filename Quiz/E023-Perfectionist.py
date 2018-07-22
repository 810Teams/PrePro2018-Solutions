"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    if num <= 0:
        print('Not Perfect')
    elif num <= 100 and num % 5 == 0:
        print('Perfect')
    elif num > 100 and (num % 10 == 0 or num % 25 == 0):
        print('Perfect')
    else:
        print('Not Perfect')

main()
