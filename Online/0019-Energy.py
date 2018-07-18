"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    distance, energy = float(input())*1000, int(input())*10
    print(int(distance//energy) + (distance % energy > 0))

main()
