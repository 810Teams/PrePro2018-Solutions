"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    stat(1, int(input()), int(input()), int(input()), int(input()))
    stat(2, int(input()), int(input()), int(input()), int(input()))
    stat(3, int(input()), int(input()), int(input()), int(input()))
    stat(4, int(input()), int(input()), int(input()), int(input()))
    stat(5, int(input()), int(input()), int(input()), int(input()))

def stat(day, hour, minute, count, loudness):
    """ Daily Wake-up Status """
    awake = 60*hour + minute
    reach = awake + 10*(count + 5 - loudness) + 55
    used = reach - awake

    print('[Day %02i]' % day, end=' ')
    print('%02i:%02i' % (awake//60, awake%60), end=' - ')
    print('%02i:%02i' % (reach//60, reach%60), end=' ')
    print('(Time Used: %i Hour(s) %i Minute(s))' % (used//60, used%60))

main()
