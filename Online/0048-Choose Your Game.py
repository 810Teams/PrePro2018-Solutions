"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    money = int(input())

    if money >= 2100:
        print('Detroit: Become Human')
        money -= 2100
    if money >= 1499:
        print('Grand Theft Auto V')
        money -= 1499
    if money >= 1399:
        print('Overwatch')
        money -= 1399
    if money >= 945:
        print('Minecraft: Java Edition')
        money -= 945
    if money >= 315:
        print('Stardew Valley')
        money -= 315

main()
