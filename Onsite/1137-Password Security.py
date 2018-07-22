"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    score = 0
    failed = 0

    while True:
        password = input()

        if len(password) < 6 and failed == 0:
            print('try again')
            failed += 1
            continue
        elif len(password) < 6 and failed == 1:
            print('process terminated')
            break

        if password.isdigit():
            score += 50
        if password.isalpha():
            score += 30
        if password.isalpha() and password.islower():
            score += 100
        if password.isalpha() and password.isupper():
            score += 85
        if password.isalnum() and not (password.isalpha() or password.isdigit()):
            score += 75
        if password.isalpha() and not (password.isupper() or password.islower()):
            score += 175
        score -= max(password.count(password[0]) - 4, 0)*15
        score += max(len(password) - 10, 0)*10
        score += ord(password[-1])

        print('Password : {}'.format('*' * len(password)))
        print('Security score : {}'.format(score))

        if score < 150:
            print('Security level : poor')
        elif score < 300:
            print('Security level : acceptable')
        else:
            print('Security level : secure')
        break

main()
