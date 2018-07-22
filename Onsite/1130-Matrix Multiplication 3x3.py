"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    size_p, size_q, size_r = 3, 3, 3

    matrix_a = [[int(input()) for _ in range(size_q)] for _ in range(size_p)]
    matrix_b = [[int(input()) for _ in range(size_r)] for _ in range(size_q)]
    matrix_r = [[multiply(matrix_a, matrix_b, i, j) for j in range(size_r)] for i in range(size_p)]

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
