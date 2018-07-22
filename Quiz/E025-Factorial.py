"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    print(factorial(int(input())))

def factorial(num):
    """ Factorial """
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)

main()
