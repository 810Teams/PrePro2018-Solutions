"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    total = 0
    students = int(input())

    for _ in range(students):
        total += float(input())

    print('Average is %.2f' % (total/students))

main()
