"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    value = input().upper().find('O')

    if value >= 0:
        print('O is at', value+1)
    else:
        print('There is no O here')

main()
