"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    data = {'FOOT': 5, 'LEG': 10, 'HEAD': 15, 'DOWN': 0, 'END LEAW GUN': 0}
    acts = list()
    score, down, passed, passed_scr = 0, 0, False, 100

    while down < 3:
        acts.append(input().upper())
        if acts[-1] in data:
            score += data[acts[-1]]

        if acts[-1] == 'DOWN':
            if score >= passed_scr:
                passed, passed_scr = True, score
            score = 0
            down += 1
            continue
        if len(acts) >= 2 and acts[-2] == 'FOOT' and acts[-1] == 'HEAD':
            score += 2
        if len(acts) >= 2 and acts[-2] == 'LEG' and acts[-1] == 'HEAD':
            score += 3
        if len(acts) >= 3 and acts[-3] == 'FOOT' and acts[-2] == 'LEG' and acts[-1] == 'HEAD':
            score += 15
        if len(acts) >= 2 and acts[-2] == 'HEAD' and acts[-1] == 'FOOT':
            score -= 10
        if acts[-1] == 'END LEAW GUN':
            break

    if score >= passed_scr:
        passed, passed_scr = True, score

    if passed:
        print('P\'GUNGUN can pass and score is', passed_scr)
    else:
        print('P\'GUNGUN Not pass')

main()
