"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    for i in input():
        alpha = ord(i)
        if chr(alpha).isalpha():
            alpha -= 3
            if not chr(alpha).isalpha():
                alpha += 26
        print(chr(alpha), end='')

    print()

main()
