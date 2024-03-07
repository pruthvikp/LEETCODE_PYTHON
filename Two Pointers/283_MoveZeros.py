'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
 
Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 
Follow up: Could you minimize the total number of operations done?
'''

# Appraoch 1
# Iterate through the array, and whenever a zero is encountered, find the next non-zero element and swap their positions.
# This process is repeated until all zeros are moved to the end.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        while i<len(nums):
            if nums[i]==0:
                j=i+1
                while j<len(nums) and nums[j]==0:
                    j+=1
                if j==len(nums):
                    j-=1
                nums[i],nums[j]=nums[j],nums[i]
            i+=1

# Approach 2:
# Initialize an index variable to keep track of the position where non-zero elements should be placed.
# Iterate through the array, and whenever a non-zero element is encountered, place it at the current index and increment the index.
# After processing all non-zero elements, fill the remaining positions in the array with zeros.
class Solution(object):
    def moveZeroes(self, nums):
        index=0
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1
        while index < len(nums):
            nums[index] = 0
            index += 1
