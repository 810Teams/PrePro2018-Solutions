"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    minutes = int(input())
    nut, palm, kate = int(input()), int(input()), int(input())
    turn, skip = 0, 0

    while turn < minutes:
        if (turn + skip) % 3 == 0:
            if nut == max(nut, palm, kate):
                skip += 1
            else:
                nut = climb(nut, palm, kate)
                turn += 1
        elif (turn + skip) % 3 == 1:
            if palm == max(nut, palm, kate):
                skip += 1
            else:
                palm = climb(palm, nut, kate)
                turn += 1
        elif (turn + skip) % 3 == 2:
            if kate == max(nut, palm, kate):
                skip += 1
            else:
                kate = climb(kate, nut, palm)
                turn += 1

    print(nut)
    print(palm)
    print(kate)

def climb(climber, person_a, person_b):
    """ Calculate jump distance for climber """
    if climber < person_a and climber < person_b:
        climber += 2*(min(person_a, person_b) - climber)
    elif person_a <= climber < person_b:
        climber += 2*(person_b - climber)
    elif person_b <= climber < person_a:
        climber += 2*(person_a - climber)

    return climber

main()














