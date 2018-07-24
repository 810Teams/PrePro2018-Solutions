"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = ''.join([str(i) for i in range(int(input()), int(input())+1)])
    for i in range(10):
        print(num.count(str(i)), end=' ')
    print()

main()
