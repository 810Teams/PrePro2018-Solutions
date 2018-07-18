"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    time = int(float(input())*1000/int(input()))
    print(time//3600, 'Hour(s)', time%3600//60, 'Minute(s)', time%60, 'Second(s)')

main()
