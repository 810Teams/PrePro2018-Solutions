"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    music_old = input().split(', ')
    music_new = list()

    for i in music_old:
        if i.lower() not in [j.lower() for j in music_new]:
            music_new.append(i)

    music_new.sort(key=len, reverse=True)
    _ = [print('{}.{}'.format(i+1, music_new[i])) for i in range(len(music_new))]

main()
