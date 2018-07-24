"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    for _ in range(int(input())):
        print(minstep(int(input())))

def minstep(num):
    """ Min step to one """
    total = 0

    while num > 1:
        if num % 3 == 0:
            num //= 3
            total += 1
        elif num % 2 == 0:
            num //= 2
            total += 1
        else:
            num -= 1
            total += 1

    return total

main()
