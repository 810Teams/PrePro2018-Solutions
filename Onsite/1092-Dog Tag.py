"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    name = input()

    print('/' + '-' * 8 + '\\')
    print('|' + name[0:8].center(8) + '|')
    print('\\' + '-' * 8 + '/')

main()
