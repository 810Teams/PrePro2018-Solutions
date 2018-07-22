"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    poles, visible = list(), list()

    while True:
        height = input()
        if height == 'X':
            break
        poles.append(int(height))

    visible.append(poles[-1])
    for i in range(-2, -len(poles)-1, -1):
        if poles[i] > visible[-1]:
            visible.append(poles[i])

    print(len(visible))
    print(*sorted(visible, reverse=True))

main()










