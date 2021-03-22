'''
# # # # # # # #
# . . . . . . #
# . # # # . . #
# . . . # . # #
# X # . . . . #
# # # # # # # #

asumme user 'X' is in coordinat (4,1)

input : 
output : 
    1. List of possible treasure location
    2. Grid with $ as possible treasure location
'''


def getTreasure():

    # Define symbol
    # B -> Bound
    # P -> Point
    # T -> Treasure possible location
    # U -> User
    # N -> Treasure not possible location

    B = '#'
    P = '.'
    T = '$'
    U = 'X'
    N = '-'

    # Land matriks
    land = [[B, B, B, B, B, B, B, B], [B, P, P, P, P, P, P, B],
            [B, P, B, B, B, P, P, B], [B, P, P, P, B, P, B, B],
            [B, U, B, P, P, P, P, B], [B, B, B, B, B, B, B, B]]

    # Teasure probability matriks
    trs = [[B, B, B, B, B, B, B, B], [B, N, N, N, N, N, N, B],
           [B, N, B, B, B, N, N, B], [B, N, N, N, B, N, B, B],
           [B, U, B, N, N, N, N, B], [B, B, B, B, B, B, B, B]]

    rowLength = len(land)
    colLength = len(land[0])

    coorList = []

    # Scan with designed window
    for row in range(1, rowLength - 1):
        for col in range(1, colLength - 1):

            if land[row][col] is not U:
                if not (((land[row - 1][col - 1] is B) and
                         (land[row - 1][col] is B) and
                         (land[row - 1][col + 1] is B) and
                         (land[row][col - 1] is B) and
                         (land[row][col + 1] is B) and
                         (land[row + 1][col] is B)) or
                        ((land[row - 1][col - 1] is P) and
                         (land[row - 1][col] is B) and
                         (land[row - 1][col + 1] is P) and
                         (land[row][col - 1] is P) and
                         (land[row][col + 1] is P) and
                         (land[row + 1][col] is B)) or
                        ((land[row - 1][col - 1] is P) and
                         (land[row - 1][col] is B) and
                         (land[row - 1][col + 1] is B) and
                         (land[row][col - 1] is P) and
                         (land[row][col + 1] is B) and
                         (land[row + 1][col] is B))):

                    if land[row][col] is not B:
                        trs[row][col] = T

                        xy = [row, col]
                        coorList.append(xy)

    print('List of possible treasure location\n')
    print(coorList)

    print('\n')

    for row in range(rowLength):
        for col in range(colLength):
            print(trs[row][col], end=' ')

        print('\n')


getTreasure()