'''
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
'''

# Brief Approach:
# Initialize an empty list new to store the transposed matrix with the number of rows and columns swapped.
# Iterate through the columns of the original matrix (n columns) and then through the rows (m rows).
# Append the corresponding element from the original matrix to the transposed matrix in the correct position. Return the transposed matrix.

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        new=[]
        m=len(matrix)
        n=len(matrix[0])
        for _ in range(n):
            new.append([])
        for i in range(n):
            for j in range(m):
                new[i].append(matrix[j][i])
        return new
