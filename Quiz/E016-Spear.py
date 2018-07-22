"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())//2+1

    for i in range(1, num+1):
        print(' '*(num-i) + '*' + ' '*((i-1)*2-1) + '*'*(i != 1))

    for i in range(num-1, 0, -1):
        print(' '*(num-i) + '*' + ' '*((i-1)*2-1) + '*'*(i != 1))

    for _ in range(num*2-1):
        print(' '*(num-1) + '*')

main()
