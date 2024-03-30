'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2
 
Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

# Approach:
# It iterates through the array and maintains two variables: count to keep track of the current consecutive ones and maxi to store the maximum consecutive ones encountered so far.
# Whenever it encounters a 0, it updates maxi with the maximum of the current count and maxi, and resets count to 0.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for num in nums:
            if num==1:
                count+=1
            else:
                maxi=max(count,maxi)
                count=0
        return max(count,maxi)
