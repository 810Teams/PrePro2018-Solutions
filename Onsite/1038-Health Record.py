"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    record = ''
    record += create_record(1, input(), int(input()), int(input()), int(input()))
    record += create_record(2, input(), int(input()), int(input()), int(input()))
    record += create_record(3, input(), int(input()), int(input()), int(input()))
    record += create_record(4, input(), int(input()), int(input()), int(input()))
    record += create_record(5, input(), int(input()), int(input()), int(input()))

    print(record)

def create_record(num, name, day, month, year):
    """ Return Health Record """
    record = '** Patient No.%i **\n' % num
    record += 'Full Name: %s\n' % name
    record += 'Birthday:  %i/%i/%i\n\n' % (day, month, year)

    return record

main()
