"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    text = input()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    height = 0

    # Get chart height
    for i in alphabets:
        if text.count(i) > height:
            height = text.count(i)

    # Chart y-labels and data
    for i in range(height, 0, -1):
        print('%2i  ' % i, end='')
        for j in alphabets:
            if text.count(j) >= i:
                print('* ', end='')
            elif 0 < text.count(j) < i:
                print('  ', end='')
        print()

    # Chart x-labels
    print('    ', end='')
    for i in alphabets:
        if i in text:
            print(i, end=' ')
    print()

main()
