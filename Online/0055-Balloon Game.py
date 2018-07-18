"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    prize_cal("P'Jack", int(input()))
    prize_cal("P'Rew", int(input()))
    prize_cal("P'Pok", int(input()))
    prize_cal("P'Fight", int(input()))
    prize_cal("P'Jub", int(input()))

def prize_cal(name, score):
    """ Prize """
    if score == 10:
        prize = 'a large teddy bear.'
    elif score >= 8:
        prize = 'a teddy bear.'
    elif score >= 6:
        prize = 'a key chain.'
    elif score >= 4:
        prize = 'a notebook.'
    elif score >= 1:
        prize = 'a pen.'
    else:
        prize = 'nothing.'

    print(name, 'won', prize)

main()
