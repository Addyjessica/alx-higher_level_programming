#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for r in range(len(matrix)):
            for itm in range(len(matrix[r])):
                if itm != len(matrix[r]) - 1:
                    endspace = ' '
                else:
                    endspace = ''
                print("{:d}".format(matrix[r][itm]), end=endspace)
            print()
