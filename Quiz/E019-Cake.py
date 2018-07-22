"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num_a1, num_b1 = 0, 1

    # Adding up fractions
    for _ in range(int(input())):
        num_a2, num_b2 = int(input()), int(input())

        num_a1, num_a2 = num_a1*num_b2, num_a2*num_b1
        num_b1, num_b2 = num_b1*num_b2, num_b2*num_b1

        num_a1 += num_a2

    # Rounding off
    div = 2
    while div <= min(num_a1, num_b1):
        if num_a1 % div == 0 and num_b1 % div == 0:
            num_a1 //= div
            num_b1 //= div
            div = 2
        else:
            div += 1

    # Output
    print(int(num_a1/num_b1) + (num_a1 % num_b1 > 0))

    if num_a1 == num_b1:
        print(0)
    else:
        print('%i/%i' % (num_b1 - num_a1 % num_b1, num_b1))

main()
