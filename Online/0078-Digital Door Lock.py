"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    if is_prime(int(input())):
        print('Yes')
    else:
        print('No')

def is_prime(num):
    """ Check if num is prime number """
    if num < 2:
        return False
    elif num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

main()
