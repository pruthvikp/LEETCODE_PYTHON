'''
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

Example 1:
Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.

Example 2:
Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= nums.length
'''

# Approach:
# Initialize an empty list new to represent the 2D array.
# Iterate through the elements of the array nums.
# For each element, check if it is not present in any existing row of the 2D array. If not, add it to the first row that doesn't contain it. If the element is present in all existing rows, create a new row with only that element.
# Return the resulting 2D array.

class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        new=[]
        new.append([])
        for num in nums:
            n=len(new)
            i=0
            while i<n:
                if num not in new[i]:
                    new[i].append(num)
                    break
                else:
                    i+=1
            if i==len(new):
                new.append([num])
        return new
