"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    animals, legs = int(input()), int(input())

    # Sees all animal as birds
    cat = 0
    bird = animals

    # Calculate remaining legs
    cat += (legs - bird*2)//2
    bird -= cat

    if cat*4 + bird*2 == legs and animals*2 <= legs <= animals*4 and legs % 2 == 0:
        print(cat)
        print(bird)
    else:
        print('Impossible')

main()
