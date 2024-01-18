'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
 
Constraints:
1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
'''

# Approach 1:
# XORing a number with itself results in 0, and XORing with 0 leaves the number unchanged. 
# So, XORing all the numbers in the array will cancel out the duplicates, leaving only the single number.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result

# Approach 2:
# Check if the length of the input array nums is 1. If true, return the single element.
# Sort the array nums to bring identical elements together.
# Iterate through the sorted array, comparing adjacent elements. Return the first element that is not equal to its adjacent element.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        nums.sort()
        i=0
        while i<len(nums)-1:
            if nums[i]==nums[i+1]:
                i+=2
            else:
                return nums[i]
        return nums[i]
      
# Approach 3:
# The code uses a dictionary to keep track of the count of each element in the array. 
# Elements are added to the dictionary if not present and removed if already present. 
# Finally, the remaining element in the dictionary (the one appearing only once) is returned.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        di={}
        for num in nums:
            if num in di:
                del di[num]
            else:
                di[num]=1
        for key in di:
            return key

