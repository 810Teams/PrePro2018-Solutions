"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    score = int(input())
    rank_a, rank_b, rank_c, rank_d = input(), input(), input(), input()

    if score >= find_minscore(rank_a):
        print(rank_a)
    elif score >= find_minscore(rank_b):
        print(rank_b)
    elif score >= find_minscore(rank_c):
        print(rank_c)
    elif score >= find_minscore(rank_d):
        print(rank_d)
    else:
        print('None')

def find_minscore(faculty):
    """ Find minscore of a specific faculty """
    if faculty == 'A':
        minscore = 20000
    elif faculty == 'B':
        minscore = 17500
    elif faculty == 'C':
        minscore = 18000
    elif faculty == 'D':
        minscore = 28250
    elif faculty == 'E':
        minscore = 27000
    elif faculty == 'F':
        minscore = 25000
    elif faculty == 'G':
        minscore = 21750
    elif faculty == 'H':
        minscore = 22000

    return minscore

main()
