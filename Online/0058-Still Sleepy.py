"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    time = int(input())*60 + int(input())   # Minutes
    used = 65

    if time >= 7*60 + 30:
        used -= 10
    if time >= 7*60 + 45:
        used -= 6
    if time >= 8*60:
        used -= 9
    if time >= 8*60 + 15:
        used -= 8
    if time >= 9*60:
        print('Continued sleeping')
        return

    print('%02i:%02i - %02i:%02i' % (time//60, time%60, (time+used)//60, (time+used)%60), end=' ')
    print('(Time Used: %i Hour(s) %i Minute(s))' % (used//60, used%60))

main()
