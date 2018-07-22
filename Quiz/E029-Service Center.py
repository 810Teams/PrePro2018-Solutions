"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    row, col, area = int(input()), int(input()), int(input())

    matrix = [[int(input()) for _ in range(col)] for _ in range(row)]
    area_list = list()

    for i in range(row - (area - 1)):
        for j in range(col - (area - 1)):
            area_list.append(area_find(matrix, area, i, j))

    print(max(area_list))

def area_find(matrix, area, row_no, col_no):
    """ Find area sum """
    total = 0

    for i in range(area):
        total += sum(matrix[row_no+i][col_no:col_no+area])

    return total

main()










