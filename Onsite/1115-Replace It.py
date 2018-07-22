"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    mylist = [input() for _ in range(int(input()))]
    index = int(input())
    mylist[index] = input()
    print(mylist)

main()
