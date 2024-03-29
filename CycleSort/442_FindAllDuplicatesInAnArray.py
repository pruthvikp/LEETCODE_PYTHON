'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Constraints:
n == nums.length
1 <= n <= 105
1 <= nums[i] <= n
Each element in nums appears once or twice.
'''

# The approach used here is based on swapping elements to their corresponding indices, as the elements in the array are positive integers ranging from 1 to n.
# The duplicate elements will occupy the position of the elements which are not present in the array.
# After the swapping is done, iterate through the array again to find elements that are not in their correct positions. These elements correspond to duplicates.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums):
            check=nums[i]-1
            if nums[i]!=nums[check]:
                nums[i],nums[check]=nums[check],nums[i]
            else:
                i+=1
        res=[]
        for i,num in enumerate(nums):
            if num!=i+1:
                res.append(num)
        return res
