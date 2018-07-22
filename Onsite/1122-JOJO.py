"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    data = input().upper().split()

    if data.count('MUDA') > 0:
        print('MUDA '*data.count('MUDA'))
    if data.count('ORA') > 0:
        print('ORA '*data.count('ORA'))

    if data.count('MUDA') > data.count('ORA'):
        print('GOODBYE JOJO!')
    elif data.count('MUDA') < data.count('ORA'):
        print('Yare Yare Daze')
    elif data.count('MUDA') == data.count('ORA') == 0:
        print('Menacing')
    elif data.count('MUDA') == data.count('ORA'):
        print('WR' + 'Y'*data.count('MUDA'))

main()
