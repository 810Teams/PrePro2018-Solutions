"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    grail = 0
    level = {5: 90, 4: 80, 3: 70, 2: 65, 1: 60}[int((input()))]
    target = int(input())

    while level < min(target, 100):
        if level == 60:
            level += 10
            grail += 1
        elif 65 <= level <= 85:
            level += 5
            grail += 1
        elif level >= 90:
            level += 2
            grail += 1

    print('Result: Level {}'.format(level))
    print('Holy Grail used: {}'.format(grail))

main()
