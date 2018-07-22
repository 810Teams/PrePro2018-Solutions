"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    europe = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark']
    europe += ['Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy']
    europe += ['Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal']
    europe += ['Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'United Kingdom']

    data = sorted([[input().title() for _ in range(3)] for _ in range(int(input()))])

    for i in data:
        if i[2] in europe:
            print('{} in {}, {}'.format(i[0], i[1], i[2]))

main()
