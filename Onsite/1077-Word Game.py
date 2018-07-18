"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    ans = input()
    score = 100

    for _ in range(20):
        if input() == ans:
            break
        else:
            score -= 5

    if score > 0:
        print('Correct!! You\'ve %i points remaining.' % score)
    else:
        print('Game Over!')

main()
