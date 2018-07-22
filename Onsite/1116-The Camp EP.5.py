"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    prohibited = ['addictive substances', 'cigarettes', 'weapons', 'alcohol', 'illegal items']
    mylist = [input() for i in range(int(input()))]
    mylist = [print(i.lower()) for i in mylist if i.lower() not in prohibited]

main()
