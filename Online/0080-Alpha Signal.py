"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    for i in input():
        if i == ' ':
            print()
        elif 'A' <= i <= 'Z':
            print('*' * (ord(i)-ord('A')+1))
        elif 'a' <= i <= 'z':
            print('*' * (ord(i)-ord('a')+1))

main()
