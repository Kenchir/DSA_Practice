"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
1   0   3
0   5   6
7   8   9

1   0   3
0   0   0
7   0   9
"""
import pprint


def zero_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rows_0 = [False] * rows
    cols_0 = [False] * cols
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rows_0[i] = True
                cols_0[j] = True
    
    for i in range(len(rows_0)):
        if rows_0[i]:
            for j in range(cols):
                matrix[i][j] = 0
    
    for i in range(len(cols_0)):
        if cols_0[i]:
            for j in range(rows):
                matrix[j][i] = 0
    
    return  matrix

    
f = [
    [1,   0,   3],
    [4,  5,   6],
    [7,   8,   9]
]

pprint.pprint(zero_matrix(f))
                    
                    


        
