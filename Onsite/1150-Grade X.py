"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    db_grade = {4: 'A', 3.5: 'B+', 3: 'B', 2.5: 'C+', 2: 'C', 1.5: 'D+', 1: 'D', 0: 'F'}
    db_student = dict()

    amount = int(input())
    gpa_old, credit_old = 0, 0

    for _ in range(amount):
        subj_id, name, credit = input(), input(), int(input())
        db_student[subj_id] = [name, credit, None]

    for _ in range(amount):
        subj_id, gpa_new = input(), float(input())
        db_student[subj_id][2] = grade_cal(gpa_old, credit_old, gpa_new, db_student[subj_id][1])

        gpa_old = gpa_new
        credit_old += db_student[subj_id][1]

    for i in sorted(db_student):
        print('{}\t{}\t{}'.format(i, db_student[i][0], db_grade[db_student[i][2]]))

def grade_cal(gpa_old, credit_old, gpa_new, credit_new):
    """ Calculate grade from GPA """
    return (gpa_new*(credit_old + credit_new) - gpa_old*credit_old)/credit_new

main()
