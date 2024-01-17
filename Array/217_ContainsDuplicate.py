'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

# The approach is to sort the array and then iterate through it, checking for consecutive equal elements. 
# If any such elements are found, the function returns True, indicating that there are duplicates. Otherwise, it returns False.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums=sorted(nums)
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                return True
            i+=1
        return False
