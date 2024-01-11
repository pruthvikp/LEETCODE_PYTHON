'''
Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
 
Constraints:
1 <= numRows <= 30
'''

'''
Approach:
- Initialize an empty list new to store the rows of Pascal's Triangle.
- Loop through numRows times to create the rows.
- For each row, append an empty list to new.
- Set the first element of each row to 1 (new[0].append(1)).
- Use nested loops to calculate the elements of each row based on the previous row.
- For each row (starting from the second row), set the first element to 1.
- Use a loop to iterate through the elements of the previous row (new[i-1]) and calculate the sum of adjacent elements.
- Append the calculated sum to the current row.
- Set the last element of each row to 1.
- Return the generated list new, representing Pascal's Triangle.
'''

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        new=[]
        for _ in range(numRows):
            new.append([])
        new[0].append(1)
        for i in range(1,numRows):
            new[i].append(1)
            for j in range(len(new[i-1])-1):
                new[i].append(new[i-1][j]+new[i-1][j+1])
            new[i].append(1)
        return new
