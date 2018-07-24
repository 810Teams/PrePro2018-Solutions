"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    diffy = [int(input()), int(input()), int(input()), int(input())]
    temp = [i for i in diffy]
    turns = 0

    print('\t'.join([str(i) for i in diffy]))

    while diffy != [0, 0, 0, 0]:
        temp[0] = abs(diffy[0] - diffy[1])
        temp[1] = abs(diffy[1] - diffy[2])
        temp[2] = abs(diffy[2] - diffy[3])
        temp[3] = abs(diffy[3] - diffy[0])
        diffy = [i for i in temp]
        turns += 1

        print('\t'.join([str(i) for i in diffy]))

    print(turns)

main()
