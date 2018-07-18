"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num_a, num_b = int(input()), int(input())

    if num_a < num_b:
        print('Too High')
    elif num_a > num_b:
        print('Too Low')
    else:
        print('Correct!')

main()
