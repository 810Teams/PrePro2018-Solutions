"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    chili, level, table = int(input()), input(), int(input())

    if level == 'MILD':
        chili -= 1000*table
    elif level == 'MEDIUM':
        chili -= 2000*table
    elif level == 'SPICY':
        chili -= 3000*table

    if chili >= 0:
        print('Enough')
        print(chili)
    else:
        print('Not Enough')

main()
