"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    for i in range(2, 37):
        print('Base {}: {}'.format(i, num_base(num, i)))

def num_base(num, base):
    """ Calculate number base """
    data = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    answer = str()

    while num >= base:
        answer += data[num % base]
        num //= base

    answer += data[num % base]

    return answer[::-1]

main()
