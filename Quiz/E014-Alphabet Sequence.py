"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    hour, minute = int(input()), int(input())

    if hour > 23 or hour < 0 or minute > 59 or minute < 0:
        print('Invalid Time')
    elif hour < 12:
        print('%i:%02i AM' % (hour, minute))
    elif hour == 12:
        print('%i:%02i PM' % (hour, minute))
    elif hour > 12:
        print('%i:%02i PM' % (hour-12, minute))

main()
