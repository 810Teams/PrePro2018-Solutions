"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    sentence = input()
    target = input()

    if target in sentence:
        print('Did someone say %s?' % target)
    else:
        print('That didn\'t work.')

main()
