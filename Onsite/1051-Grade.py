"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    score = int(input())

    if 0 <= score < 50:
        print(0)
    elif 50 <= score < 55:
        print(1)
    elif 55 <= score < 60:
        print(1.5)
    elif 60 <= score < 65:
        print(2)
    elif 65 <= score < 70:
        print(2.5)
    elif 70 <= score < 75:
        print(3)
    elif 75 <= score < 80:
        print(3.5)
    elif 80 <= score <= 100:
        print(4)
    else:
        print('Invalid')

main()
