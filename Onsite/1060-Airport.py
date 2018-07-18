"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    method = input()
    time = 60*int(input()) + int(input())

    # PM Format
    if input() == 'pm' and (time < 12*60):
        time += 12*60

    # Travel methods
    if method == 'A':
        time -= 15 + 5 + 70 + 25 + 45
    elif method == 'B':
        time -= 10 + 70 + 15 + 45
    elif method == 'C':
        time -= 65 + 5 + 45

    # Calculation
    time %= 24*60

    if time < 12*60:
        print('%02i:%02iam' % (time//60, time%60))
    elif 12*60 <= time < 13*60:
        print('%02i:%02ipm' % (time//60, time%60))
    else:
        time -= 12*60
        print('%02i:%02ipm' % (time//60, time%60))

main()
