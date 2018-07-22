"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num_x, num_y = 0, 0
    target_x, target_y = [int(i) for i in input().strip('()').split(', ')]
    atp_a, atp_b = int(input().replace(' ATP', '')), int(input().replace(' ATP', ''))
    energy = 0

    # Diagonal walk
    if atp_a*2 >= atp_b:
        energy += atp_b * min(target_x, target_y)
    else:
        energy += 2 * atp_a * min(target_x, target_y)
    num_x += min(target_x, target_y)
    num_y += min(target_x, target_y)

    # Straight walk
    if atp_a <= atp_b:
        # True Straight
        energy += atp_a * max(target_x - num_x, target_y - num_y)
        num_x += target_x - num_x
        num_y += target_y - num_y
    elif atp_a > atp_b:
        # Double Diagonal
        energy += atp_b * (max(target_x - num_x, target_y - num_y)//2*2)
        num_x += (target_x - num_x)//2*2
        num_y += (target_y - num_y)//2*2

        if target_x - num_x > 0 or target_y - num_y > 0:
            energy += atp_a

    print(energy, 'ATP')

main()










