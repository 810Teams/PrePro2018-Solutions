"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    people = ('Yes' in input()) + ('Yes' in input()) + ('Yes' in input())
    people += ('Yes' in input()) + ('Yes' in input())

    if people == 5:
        print('Superstar')
    elif people == 4:
        print('Very Popular')
    elif people == 3:
        print('Popular')
    elif people >= 1:
        print('Ordinary Student')
    elif people == 0:
        print('Invisible')

main()
