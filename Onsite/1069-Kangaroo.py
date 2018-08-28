"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    pos_a, jump_a = int(input()), int(input())
    pos_b, jump_b = int(input()), int(input())

    # Case: Kangaroo 2 always be ahead
    if pos_b > pos_a and jump_b >= jump_a:
        print('NO')
        return

    # Start Jumping
    while pos_b > pos_a:
        pos_a += jump_a
        pos_b += jump_b

    # Output
    if pos_a == pos_b:
        print('YES')
        print(jumps)
    else:
        print('NO')

main()
