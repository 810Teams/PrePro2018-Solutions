"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    start = int(input())

    name_ls = ''
    name_ls += create_five(start + 0)
    name_ls += create_five(start + 5)
    name_ls += create_five(start + 10)
    name_ls += create_five(start + 15)
    name_ls += create_five(start + 20)
    name_ls += create_five(start + 25)
    name_ls += create_five(start + 30)
    name_ls += create_five(start + 35)
    name_ls += create_five(start + 40)
    name_ls += create_five(start + 45)

    print(name_ls)

def create_five(start):
    """ Create 5 Name List Items """
    name_ls = ''
    name_ls += 'ID#%i\t%s\n' % (start + 0, input())
    name_ls += 'ID#%i\t%s\n' % (start + 1, input())
    name_ls += 'ID#%i\t%s\n' % (start + 2, input())
    name_ls += 'ID#%i\t%s\n' % (start + 3, input())
    name_ls += 'ID#%i\t%s\n' % (start + 4, input())

    return name_ls

main()
