"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    timecal(int(input()), int(input()), int(input()), 1)
    timecal(int(input()), int(input()), int(input()), 2)
    timecal(int(input()), int(input()), int(input()), 3)
    timecal(int(input()), int(input()), int(input()), 4)
    timecal(int(input()), int(input()), int(input()), 5)
    timecal(int(input()), int(input()), int(input()), 6)
    timecal(int(input()), int(input()), int(input()), 7)
    timecal(int(input()), int(input()), int(input()), 8)
    timecal(int(input()), int(input()), int(input()), 9)
    timecal(int(input()), int(input()), int(input()), 10)

def timecal(hour, minute, lazy, day):
    """ Time Calculator """
    time = 60*hour + minute
    time += 65 + 6*lazy

    print("[Day %02i] %02i:%02i - %02i:%02i" % (day, hour, minute, time//60, time%60), end=' ')
    print("(Time Used: %i Hour(s) %i Minute(s))" % ((65 + 6*lazy)//60, (65 + 6*lazy)%60))

main()
