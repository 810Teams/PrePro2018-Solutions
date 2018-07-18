"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num_a, num_b, num_c, num_d = int(input()), int(input()), int(input()), int(input())

    num_a, num_b = max(num_a, num_b), min(num_a, num_b)

    num_b, num_c = max(num_b, num_c), min(num_b, num_c)
    num_a, num_b = max(num_a, num_b), min(num_a, num_b)

    num_c, num_d = max(num_c, num_d), min(num_c, num_d)
    num_b, num_c = max(num_b, num_c), min(num_b, num_c)
    num_a, num_b = max(num_a, num_b), min(num_a, num_b)

    print(num_a)
    print(num_b)
    print(num_c)
    print(num_d)

main()
