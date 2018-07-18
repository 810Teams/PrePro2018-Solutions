"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    if num % 2 == 1:
        print('Oooo')
    elif 2 <= num <= 5:
        print('lelelel')
    elif 6 <= num <= 20:
        print('OMG!')
    elif num > 20:
        print('Infinite!')
    else:
        print('Out of condition!')

main()
