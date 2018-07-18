"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num_a, num_b = float(input()), float(input())
    num_a, num_b = min(num_a, num_b), max(num_a, num_b)

    area = ((num_b**3)/3 + num_b) - ((num_a**3)/3 + num_a)

    print("%.2f" % area)

main()
