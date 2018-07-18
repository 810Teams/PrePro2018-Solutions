"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num_a, num_b = int(input()), int(input())

    for i in range(min(num_a, num_b), 0, -1):
        if num_a % i == 0 and num_b % i == 0:
            print(i)
            break

main()
