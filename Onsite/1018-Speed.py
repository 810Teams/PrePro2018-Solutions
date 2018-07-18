"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    speed = int(input())/int(input())
    speed *= 60*60  # Convert seconds to hour
    speed /= 1000   # Convert meters to kilometers

    print('%.2f' % speed)

main()
