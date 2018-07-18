"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    score = float(input())

    if score >= 90:
        print('A')
    elif score >= 80:
        print('B+')
    elif score >= 75:
        print('B')
    elif score >= 67:
        print('C+')
    elif score >= 50:
        print('C')
    elif score >= 40:
        print('D+')
    elif score >= 30:
        print('D')
    else:
        print('F')

main()
