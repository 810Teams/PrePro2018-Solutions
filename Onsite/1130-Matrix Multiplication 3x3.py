"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    matrix_a = [[int(input()) for _ in range(3)] for _ in range(3)]
    matrix_b = [[int(input()) for _ in range(3)] for _ in range(3)]
    matrix_r = [[multiply(matrix_a, matrix_b, i, j) for j in range(3)] for i in range(3)]

    for i in matrix_r:
        for j in i:
            print(j, end=' ')
        print()

def multiply(matrix_a, matrix_b, select_row_a, select_col_b):
    """ Multiply a row from matrix_a with a column from matrix_b """
    row = matrix_a[select_row_a]
    col = [i[select_col_b] for i in matrix_b]

    return sum([row[i]*col[i] for i in range(len(row))])

main()
