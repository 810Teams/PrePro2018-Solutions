"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num_a, num_b = 0, 1

    for _ in range(int(input())):
        num_a, num_b = num_b, num_a + num_b

    print(num_a)

main()
