"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    for _ in range(num):
        print('***'*num + ' '*num + '***'*num)

    for _ in range(num*2):
        print(' '*num + '*'*num + '   '*num + '*'*num + ' '*num)

    for _ in range(num):
        print('***'*num + '  '*num + '*'*num + ' '*num)

main()
