"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    match(1, input(), int(input()), input(), int(input()))
    match(2, input(), int(input()), input(), int(input()))
    match(3, input(), int(input()), input(), int(input()))
    match(4, input(), int(input()), input(), int(input()))
    match(5, input(), int(input()), input(), int(input()))
    match(6, input(), int(input()), input(), int(input()))

def match(num, team_a, score_a, team_b, score_b):
    """ Match calculator """
    print('Match #%i:' % num, end=' ')
    print(team_a*(score_a > score_b) + team_b*(score_a < score_b) + 'Tie!'*(score_a == score_b))

main()
