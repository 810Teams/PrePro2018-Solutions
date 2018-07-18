"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    target = int(input())
    saint = int(input())
    gunn = int(input())
    saint += int(input())
    gunn += int(input())
    saint += int(input())
    gunn += int(input())

    if abs(target-saint) < abs(target-gunn):
        print('Saint won!')
    elif abs(target-saint) > abs(target-gunn):
        print('Gunn won!')
    else:
        print('Draw!')

main()
