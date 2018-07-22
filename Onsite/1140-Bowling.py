"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    scoreboard = input()
    last_frame = len(scoreboard.split()[-1])
    scoreboard = list(scoreboard.replace(' ', ''))
    score = 0

    # Data re-structuring
    for i in range(len(scoreboard)):
        if scoreboard[i] == '-':
            scoreboard[i] = ('-', 0)
        elif scoreboard[i] == 'X':
            scoreboard[i] = ('X', 10)
        elif scoreboard[i] == '/':
            scoreboard[i] = ('/', 10-scoreboard[i-1][1])
        else:
            scoreboard[i] = (scoreboard[i], int(scoreboard[i]))

    # Score calculation: First 9 frames
    for i in range(len(scoreboard) - last_frame):
        if scoreboard[i][0] == 'X':
            score += scoreboard[i][1] + scoreboard[i + 1][1] + scoreboard[i + 2][1]
        elif scoreboard[i][0] == '/':
            score += scoreboard[i][1] + scoreboard[i + 1][1]
        else:
            score += scoreboard[i][1]

    # Score calculation: Last frame
    for i in range(len(scoreboard) - last_frame, len(scoreboard)):
        score += scoreboard[i][1]

    print(score)

main()
