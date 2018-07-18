"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    people = 0
    unlocked = False

    while True:
        action = input()
        if action == '-1':
            break
        elif action == 'S':
            unlocked = True
        elif action == 'E' and unlocked:
            people += 1
            unlocked = False

    print(people)

main()
