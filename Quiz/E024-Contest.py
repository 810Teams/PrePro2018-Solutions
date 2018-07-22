"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    gender, name = input(), input()
    age, tall, mass, spc = int(input()), int(input()), float(input()), int(input())

    if gender == 'Male':
        if 19 < age < 31 and tall >= 175 and 55 <= mass <= 80 and spc >= 1:
            print('Mr.{} passed the 1st round.'.format(name))
        else:
            print('Mr.{} didn\'t pass the 1st round.'.format(name))

    elif gender == 'Female':
        if input() != "Yes" and 18 < age < 29 and tall >= 160 and 40 <= mass <= 65 and spc >= 2:
            print('Miss {} passed the 1st round.'.format(name))
        else:
            print('Miss {} didn\'t pass the 1st round.'.format(name))

main()
