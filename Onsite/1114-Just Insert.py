"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    mylist = [input() for _ in range(int(input()))]
    mylist.insert(int(input()), input())
    print(mylist)

main()
