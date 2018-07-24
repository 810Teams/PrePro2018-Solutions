"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    shift = int(input()) % 26

    for i in input():
        alpha = ord(i)

        if chr(alpha).isupper():
            alpha -= shift
            if not chr(alpha).isupper():
                alpha += 26
        elif chr(alpha).islower():
            alpha -= shift
            if not chr(alpha).islower():
                alpha += 26

        print(chr(alpha), end='')

    print()

main()
