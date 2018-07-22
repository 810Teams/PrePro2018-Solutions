"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    size_i, size_j = [int(i) for i in input().split('x')]
    matrix_a = [[int(input()) for _ in range(size_j)] for _ in range(size_i)]
    matrix_b = [[int(input()) for _ in range(size_j)] for _ in range(size_i)]
    matrix_r = [[matrix_a[i][j] + matrix_b[i][j] for j in range(size_j)] for i in range(size_i)]

    for i in matrix_r:
        for j in i:
            print(j, end=' ')
        print()

main()
