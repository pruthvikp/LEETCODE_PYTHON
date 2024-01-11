'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
0 <= rowIndex <= 33
'''

'''
Approach:

- Initialize an empty list result with the first element set to 1 (result=[1]).
- Initialize a variable prev to 1, representing the value of the previous element in the row.
- Use a for loop to iterate from 1 to rowIndex.
- Inside the loop, calculate the next value using the formula prev * (rowIndex-k+1)//k, where k is the loop variable.
- Append the calculated nextval to the result list.
- Update the prev variable with the calculated nextval.
- Return the generated list result, representing the rowIndex-th row of Pascal's Triangle.
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result=[1]
        prev=1
        for k in range(1,rowIndex+1):
            nextval=prev * (rowIndex-k+1)//k
            result.append(nextval)
            prev=nextval
        return result
