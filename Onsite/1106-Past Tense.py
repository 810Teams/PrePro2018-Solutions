"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    text = input()
    text = text.replace(' is ', ' was ').replace(' are ', ' were ')
    text = text.replace('Is ', 'Was ').replace('Are ', 'Were ')

    print(text)

main()
