"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    text = input()

    if 'first' in text and 'ror' in text and 'mak' in text:
        print("P'First ror mak mak!!")
    elif ('first' in text or 'ror' in text) and 'mak' in text:
        print("I think so!!")
    elif 'first' in text and 'ror' in text:
        print("I'm so First!!")
    else:
        print("First == ror -> is always True!!")

main()
