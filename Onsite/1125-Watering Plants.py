"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    days = int(input())
    trees = [days for _ in range(int(input()))]
    days = 0

    while True:
        water = int(input())
        trees.sort(reverse=True)

        for i in range(len(trees)-water):
            trees[i] -= 1

        if water > len(trees)*4:
            trees.append(0)

        if 0 not in trees:
            days += 1
        else:
            break

    print(days)

main()
