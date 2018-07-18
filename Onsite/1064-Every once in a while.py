"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())
    step = int(input())

    if num > 0:
        for i in range(1, num+1, step):
            print(i)
    else:
        for i in range(-1, num-1, -step):
            print(i)

main()
