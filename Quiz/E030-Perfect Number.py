"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    total, num = 0, 1
    target = int(input())

    while equation(num) <= target:
        if is_prime(2**num - 1):
            total += equation(num)
        num += 1

    print(total)

def is_prime(num):
    """ Check if num is prime number """
    if num < 2:
        return False
    elif num == 2:
        return True

    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False

    return True

def equation(num):
    """ Perfect number equation """
    return 2**(num-1) * (2**num - 1)

main()










