'''
Given an m x n binary matrix mat, return the number of special positions in mat.
A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).

Example 1:
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.
 
Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.
'''

# Approach:
# Initialize a variable splcnt to 0 to count the number of special positions.
# Iterate through each element in the matrix using nested loops.
# If the current element is 1, calculate the sum of the elements in its row and column.
# If the sum of the row is 1 and the sum of the column is 1, increment splcnt as this position is special.
# Return the final count of special positions.
  
class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        splcnt=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j]==1:
                    rowsum=0
                    for k in range(len(mat[i])):
                        rowsum+=mat[i][k]
                    if rowsum==1:
                        colsum=0
                        for l in range(len(mat)):
                            colsum+=mat[l][j]
                        if colsum==1:
                            splcnt+=1
        return splcnt
