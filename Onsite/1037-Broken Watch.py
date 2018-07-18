"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    result = ''
    result += timecal(int(input()))
    result += timecal(int(input()))
    result += timecal(int(input()))

    print(result)

def timecal(sec):
    """ Time calculation """
    return '%i Hour(s) %i Minute(s) %i Second(s)\n' % (sec//3600, (sec%3600)//60, sec%60)

main()
