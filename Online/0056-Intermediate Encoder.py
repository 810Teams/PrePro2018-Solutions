"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    alpha = ord(input())-6

    if (alpha < ord('A')) or (ord('Z') < alpha < ord('a')):
        alpha += 26

    print(chr(alpha))

main()
