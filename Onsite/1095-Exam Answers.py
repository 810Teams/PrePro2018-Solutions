"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    answer, paper = input(), input()
    score = 0

    for i in range(len(answer)):
        if answer[i] == paper[i]:
            score += 1

    if score > 0:
        print('Score : {}/{}'.format(score, len(answer)))
        print('{:.2f}%'.format(score/len(answer)*100))
    else:
        print('Pokpak')

main()
