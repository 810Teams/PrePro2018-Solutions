"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    char = input()
    print(chr(ord(char) + ((char != 'Z' and char != 'z') - 25*(char == 'Z' or char == 'z'))))

main()
