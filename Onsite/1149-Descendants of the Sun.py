"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

# Latitude is horizontal line, value changes by moving vertically.   (Similar to y-coordinates)
# Longtitude is vertical line, value changes by moving horizontally. (Similar to x-coordinates)

from math import radians, sin, cos, asin, sqrt

def main():
    """ Main function """
    output = str()
    times = int(input())
    lat_old, lon_old = [float(i) for i in input().strip('()').split(', ')]

    for i in range(1, times+1):
        lat_new, lon_new = [float(i) for i in input().strip('()').split(', ')]

        output += '#{} Distance: '.format(i)
        output += '{:.2f}km '.format(get_distance(lat_old, lon_old, lat_new, lon_new))
        output += 'Direction: {}\n'.format(get_direction(lat_old, lon_old, lat_new, lon_new))

        lat_old, lon_old = lat_new, lon_new

    print(output, end='')

def get_distance(lat_old, lon_old, lat_new, lon_new):
    """ Calculate and get distance """
    lat_old, lon_old = radians(lat_old), radians(lon_old)
    lat_new, lon_new = radians(lat_new), radians(lon_new)

    part = sin((lat_new - lat_old)/2)**2 + cos(lat_old)*cos(lat_new)*sin((lon_new - lon_old)/2)**2
    distance = 2 * 6378.137 * asin(sqrt(part))

    return distance

def get_direction(lat_old, lon_old, lat_new, lon_new):
    """ Calculate and get direction """
    direction = '-'

    if lat_new > lat_old and lon_new == lon_old:
        direction = 'N'
    elif lat_new < lat_old and lon_new == lon_old:
        direction = 'S'
    elif lat_new == lat_old and lon_new < lon_old:
        direction = 'W'
    elif lat_new == lat_old and lon_new > lon_old:
        direction = 'E'
    elif lat_new > lat_old and lon_new < lon_old:
        direction = 'NW'
    elif lat_new > lat_old and lon_new > lon_old:
        direction = 'NE'
    elif lat_new < lat_old and lon_new < lon_old:
        direction = 'SW'
    elif lat_new < lat_old and lon_new > lon_old:
        direction = 'SE'

    return direction

main()
