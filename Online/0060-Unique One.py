"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    item_a = int(input())
    item_b = int(input())
    item_c = int(input())
    item_d = int(input())
    item_e = int(input())

    if check_unique(item_a, item_b, item_c, item_d, item_e):
        print(item_a)
    elif check_unique(item_b, item_a, item_c, item_d, item_e):
        print(item_b)
    elif check_unique(item_c, item_a, item_b, item_d, item_e):
        print(item_c)
    elif check_unique(item_d, item_a, item_b, item_c, item_e):
        print(item_d)
    elif check_unique(item_e, item_a, item_b, item_c, item_d):
        print(item_e)

def check_unique(item_main, item_w, item_x, item_y, item_z):
    """ Check if the item is unique """
    if (item_main == item_w) or (item_main == item_x):
        return False
    if (item_main == item_y) or (item_main == item_z):
        return False
    return True

main()
