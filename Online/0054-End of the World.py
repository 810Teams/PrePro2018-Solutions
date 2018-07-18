"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    sentence = input()
    villain, hero = int(input()), int(input())

    if hero > villain*0.3:
        villain *= 0.55
    if sentence == 'Justify yourself!':
        villain *= 0.8

    if villain-hero <= 0:
        print('We saved the world!')
    elif villain-hero <= 1000:
        print('A great loss.')
    else:
        print('End of the world.')

main()
