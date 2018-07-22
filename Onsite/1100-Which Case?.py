"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    text = input()

    if text.isupper():
        print("This sentence is written in uppercase.")
    elif text.islower():
        print("This sentence is written in lowercase.")
    else:
        print("This sentence is written in both uppercase and lowercase.")

main()
