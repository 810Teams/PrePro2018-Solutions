"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    for _ in range(int(input())):
        for i in range(1, num+1):
            state = False
            for j in range(1, num+1):
                if i == j:
                    print('\\', end='')
                    state = not state
                elif i + j == num + 1:
                    print('/', end='')
                    state = not state
                elif state and not (num % 2 == 1 and i == num//2+1):
                    print('-', end='')
                else:
                    print(' ', end='')
            print()

main()
