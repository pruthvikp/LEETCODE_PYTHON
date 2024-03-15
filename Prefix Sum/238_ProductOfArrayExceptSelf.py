'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 
Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
'''


# The intuition here is to use two passes: one to calculate the prefix products (products to the left of each element), and another to calculate the postfix products (products to the right of each element). 
# The final result is the product of the corresponding prefix and postfix products for each element.

# Approach:
# Initialize an array output with all elements set to 1. This array will store the product of all elements except the one at the current index.
# Calculate the prefix products in the first pass. Traverse the array from left to right, updating the prefix product for each element.
# Calculate the postfix products in the second pass. Traverse the array from right to left, updating the postfix product for each element and multiplying it with the corresponding prefix product.
# Return the final output array.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prefix,postfix=1,1
        for i in range(n):
            res[i]=prefix
            prefix*=nums[i]
        for i in range(n-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
