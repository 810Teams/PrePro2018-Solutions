"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    print(fibo({0: 0, 1: 1}, int(input())))

def fibo(database, num):
    """ Recursive Fibonacci number """
    if num not in database:
        database[num] = fibo(database, num - 1) + fibo(database, num - 2)

    return database[num]

main()
