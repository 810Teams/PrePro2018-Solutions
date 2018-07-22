"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    data = [input().split(', ') for i in range(int(input()))]

    print('Total: {}'.format(sum([len(i) for i in data]) - len(data)))

    for i in data:
        print('{} at {} {}'.format(len(i[1:]), i[0], i[1:]))

main()
