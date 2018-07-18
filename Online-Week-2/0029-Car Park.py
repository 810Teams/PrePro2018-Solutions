"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    parkingfee(int(input()), float(input()), 1)
    parkingfee(int(input()), float(input()), 2)
    parkingfee(int(input()), float(input()), 3)
    parkingfee(int(input()), float(input()), 4)
    parkingfee(int(input()), float(input()), 5)
    parkingfee(int(input()), float(input()), 6)
    parkingfee(int(input()), float(input()), 7)
    parkingfee(int(input()), float(input()), 8)
    parkingfee(int(input()), float(input()), 9)
    parkingfee(int(input()), float(input()), 10)
    parkingfee(int(input()), float(input()), 11)
    parkingfee(int(input()), float(input()), 12)
    parkingfee(int(input()), float(input()), 13)
    parkingfee(int(input()), float(input()), 14)
    parkingfee(int(input()), float(input()), 15)
    parkingfee(int(input()), float(input()), 16)
    parkingfee(int(input()), float(input()), 17)
    parkingfee(int(input()), float(input()), 18)
    parkingfee(int(input()), float(input()), 19)
    parkingfee(int(input()), float(input()), 20)

def parkingfee(rate, hour, num):
    """ Calculate Parking Fee """
    print("Car No.%02i: %.2f Baht." % (num, int(hour)*rate))

main()
