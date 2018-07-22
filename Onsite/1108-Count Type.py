"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    lower, upper, number, other = 0, 0, 0, 0

    for i in input():
        if i.islower():
            lower += 1
        elif i.isupper():
            upper += 1
        elif i.isdigit():
            number += 1
        else:
            other += 1

    print('Uppercase :', upper)
    print('Lowercase :', lower)
    print('Numeric :', number)
    print('Other :', other)

main()
