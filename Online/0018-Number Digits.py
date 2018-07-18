"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num0 = int(input()) % 10
    num1 = int(input()) % 100 // 10
    num2 = int(input()) % 1000 // 100
    num3 = int(input()) % 10000 // 1000
    num4 = int(input()) // 10000
    print('%i+%i+%i+%i+%i = %i'%(num0, num1, num2, num3, num4, num0 + num1 + num2 + num3 + num4))

main()
