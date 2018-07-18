"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    current = float(input())
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))
    current = calculate(current, float(input()))

def calculate(current, change):
    """ Calculate new world line, then print """
    print("%.6f" % (current + change))
    return current + change

main()
