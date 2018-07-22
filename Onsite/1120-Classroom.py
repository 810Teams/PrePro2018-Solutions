"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    mylist = sorted([[i[1], i[0]] for i in [[input(), int(input())] for _ in range(int(input()))]])
    _ = [print(i[0], i[1]) for i in mylist]

main()
