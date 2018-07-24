"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    shift = int(input()) % 26
    alpha = ord(input())

    if chr(alpha).isupper():
        alpha -= shift
        if not chr(alpha).isupper():
            alpha += 26
    elif chr(alpha).islower():
        alpha -= shift
        if not chr(alpha).islower():
            alpha += 26

    print(chr(alpha))

main()
