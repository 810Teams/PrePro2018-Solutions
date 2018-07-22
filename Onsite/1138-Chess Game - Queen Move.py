"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    board = [['_' for _ in range(8)] for _ in range(8)]
    q_row, q_col = [int(i)-1 for i in input().split()]

    for i in range(8):
        for j in range(8):
            if abs(q_row - i) == abs(q_col - j):
                board[i][j] = '+'
            elif i == q_row or j == q_col:
                board[i][j] = '+'

    board[q_row][q_col] = 'Q'

    print(' _ _ _ _ _ _ _ _')
    for i in board:
        print('|' + '|'.join(i) + '|')

main()
