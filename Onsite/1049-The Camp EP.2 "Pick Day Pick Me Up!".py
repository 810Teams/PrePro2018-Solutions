"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    day = int(input())

    if day in (23, 24, 25):
        print('Yep! %i UNiTEC@MP3' % day)
    elif day <= 31:
        print('Try again!')
    else:
        print('404 NOT FOUND')

main()
