
'''
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

 
Input:  1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 
Explanation: The output is matrix in spiral format. 

Input:  1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output: 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
Explanation :The output is matrix in spiral format.
'''

def spiralOrder( matrix):
        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols -1
        arr =[]

        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                arr.append(matrix[top][i])

            top += 1

            for i in range(top, bottom + 1):
                arr.append(matrix[i][right])

            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    arr.append(matrix[bottom][i])

            bottom -= 1
            
            if right >= left:
                for i in range(bottom, top - 1, -1):
                    arr.append(matrix[i][left])

            left += 1

        return arr

a = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
b= [[1,2,3],
    [4,5,6],
    [7,8,9]]
print(spiralOrder(a))

        
