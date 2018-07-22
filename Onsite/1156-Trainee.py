"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    trainee_jp, trainee_kr = list(), list()

    while True:
        name = input()
        if name == 'stop':
            break
        elif len(name.split()) == 2:
            trainee_jp.append(name)
        elif len(name.split()) == 3:
            trainee_kr.append(name)

    if len(trainee_jp) > 0:
        print('{} Japanese Trainee'.format(len(trainee_jp)))
        for i in sorted(trainee_jp):
            print(i)
    else:
        print('No Japanese Trainee')

    print('----------')

    if len(trainee_kr) > 0:
        print('{} Korean Trainee'.format(len(trainee_kr)))
        for i in sorted(trainee_kr):
            print(i)
    else:
        print('No Korean Trainee')

main()
