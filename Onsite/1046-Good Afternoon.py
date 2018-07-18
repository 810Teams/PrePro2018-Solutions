"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    time = 60*int(input()) + int(input())

    if 5*60 <= time < 12*60:
        print('Good Morning')
    elif 12*60 <= time < 18*60:
        print('Good Afternoon')
    elif 18*60 <= time < 23*60:
        print('Good Evening')
    else:
        print('Good Night')

main()
