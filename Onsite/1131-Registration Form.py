"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    prefix, fname, lname, age, grade, school = input().split(', ')
    prefix = prefix[0] + prefix[-1] + '.'

    print('********************')
    print('Registration Confirm')
    print('********************')
    print('{} {} {}'.format(prefix, fname, lname))
    print('Age: {}'.format(age))
    print('Matthayom: {}'.format(grade))
    print('{} School'.format(school))
    print('********************')
    print('Thank You!')

main()
