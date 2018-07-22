"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    rank = [float(i[2]) for i in [input().split(', ') for _ in range(int(input()))]]
    print('{:.2f}'.format(sum(rank)/len(rank)))

main()
