"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    army = create_row(0)
    army += create_row(1)
    army += create_row(2)
    army += create_row(3)
    army += create_row(4)
    army += create_row(5)
    army += create_row(6)
    army += create_row(7)
    army += create_row(8)
    army += create_row(9)

    print(army, end='')

def create_row(row):
    """ Create row """
    result = ''
    result += '%s:%i#' % (input(), 5*row + 1) + '\t\t'
    result += '%s:%i#' % (input(), 5*row + 2) + '\t\t'
    result += '%s:%i#' % (input(), 5*row + 3) + '\t\t'
    result += '%s:%i#' % (input(), 5*row + 4) + '\t\t'
    result += '%s:%i#' % (input(), 5*row + 5) + '\n'
    return result

main()
