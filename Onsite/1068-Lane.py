def main():
    """ Main Function """
    lane = 1

    while True:
        turn = input()
        if turn == 'L':
            if lane != 1:
                lane -= 1
        elif turn == 'R':
            if lane != 4:
                lane += 1
        else:
            break
    print(lane)

main()