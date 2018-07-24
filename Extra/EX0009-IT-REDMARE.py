"""
Pre-Programming 61 Solution
By Teerapat Kraisrisirikul
"""

def main():
    """ Main function """
    num = int(input())

    for _ in range(num):
        pattern = '***** *****     ****  ***** ***   *   *   *   ****  *****'
        print(pattern.replace(' ', ' '*num).replace('*', '*'*num))

    for _ in range(num):
        pattern = '  *     *       *   * *     *  *  ** **  * *  *   * *'
        print(pattern.replace(' ', ' '*num).replace('*', '*'*num))

    for _ in range(num):
        pattern = '  *     *   *** ****  ***** *   * * * * ***** ****  *****'
        print(pattern.replace(' ', ' '*num).replace('*', '*'*num))

    for _ in range(num):
        pattern = '  *     *       * *   *     *  *  *   * *   * * *   *'
        print(pattern.replace(' ', ' '*num).replace('*', '*'*num))

    for _ in range(num):
        pattern = '*****   *       *  *  ***** ***   *   * *   * *  *  *****'
        print(pattern.replace(' ', ' '*num).replace('*', '*'*num))

main()
