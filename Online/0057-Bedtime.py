"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    sleep = int(input())*60 + int(input())
    awake = int(input())*60 + int(input())

    if awake <= sleep:
        awake += 24*60

    if awake - sleep < 7*60:
        print('Not enough')
    elif awake - sleep < 10*60:
        print('Enough')
    else:
        print('Too much')

main()
