"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    chance = 100 - int(input())*(int(input())-2018)
    print(chance * (chance > 0), '%')

main()
