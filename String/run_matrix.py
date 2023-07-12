def print_matrix(matrix):
    string = ''
    for i in matrix:
        for j in i:
            string += '%s\t' % j
            # print(string)
        string = string[:-1]
        string += '\n'
    string = string[:-1]
    return string

matr1 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

matr2 = [[10, 11, 12],
         [13, 14, 15],
         [16, 17, 18]]

print(print_matrix(matr2))