"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

from math import sqrt

def main():
    """ Main function """
    for i in range(1, int(input())+1):
        if is_prime(i):
            print(i)

def is_prime(num):
    """ Check if num is prime number """
    if num < 2:
        return False
    elif num == 2:
        return True

    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False

    return True

main()
