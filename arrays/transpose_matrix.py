

def transpose(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(1 + i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

    
def reverse_rows(matrix):
    n = len(matrix)
    k ="aa"
    k.isalpha()
    for i in range(n):
        l, r = 0, n - 1
        while l < r:
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
            l += 1
            r -= 1
    
    return matrix

print(reverse_rows(transpose([[1,2,3],[4,5,6],[7,8,9]])))
    