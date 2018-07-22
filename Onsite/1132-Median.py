"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = sorted([float(i) for i in input().split(', ')])

    if len(num) % 2 == 1:
        print('{:.2f}'.format(num[(len(num)-1)//2]))
    else:
        print('{:.2f}'.format((num[(len(num)-1)//2] + num[len(num)//2])/2))

main()
