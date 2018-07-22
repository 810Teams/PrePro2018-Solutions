"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman = [data[i] for i in input()]
    num = [i for i in roman]

    for i in range(len(roman)-1):
        if roman[i] < roman[i+1]:
            num[i] = 0
            num[i+1] -= roman[i]

    print(sum(num))

main()
