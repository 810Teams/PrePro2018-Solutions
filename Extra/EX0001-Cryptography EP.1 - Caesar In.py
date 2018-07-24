"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    alpha = ord(input())

    if chr(alpha).isalpha():
        alpha -= 3
        if not chr(alpha).isalpha():
            alpha += 26

    print(chr(alpha))

main()
