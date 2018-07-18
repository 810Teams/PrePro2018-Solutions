"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    target, card = input(), input()

    if target == 'Chatuchak Park' and card == 'Adult':
        price = 21
    elif target == 'Chatuchak Park' and card == 'Student':
        price = 19
    elif target == 'Chatuchak Park' and card == 'Elder':
        price = 11
    elif target == 'Phahon Yothin' and card == 'Adult':
        price = 23
    elif target == 'Phahon Yothin' and card == 'Student':
        price = 21
    elif target == 'Phahon Yothin' and card == 'Elder':
        price = 12
    elif target == 'Lat Phrao' and card == 'Adult':
        price = 25
    elif target == 'Lat Phrao' and card == 'Student':
        price = 23
    elif target == 'Lat Phrao' and card == 'Elder':
        price = 13
    elif target == 'Ratchadaphisek' and card == 'Adult':
        price = 28
    elif target == 'Ratchadaphisek' and card == 'Student':
        price = 25
    elif target == 'Ratchadaphisek' and card == 'Elder':
        price = 14

    print(price)

main()
