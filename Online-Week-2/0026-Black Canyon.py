"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    bill = 0
    bill += (int(input()) + int(input())) * 0.8
    bill += (int(input()) + int(input())) * 0.8
    bill += (int(input()) + int(input())) * 0.8
    bill += (int(input()) + int(input())) * 0.8
    bill += (int(input()) + int(input())) * 0.8
    bill *= 0.9

    print("Total : %.2f Baht" % bill)

main()
