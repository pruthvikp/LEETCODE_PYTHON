'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Example 3:
Input: nums = [3,3,3,3,3]
Output: 3
 
Constraints:
1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.
 
Follow up:
How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
'''

# Approach:
# The "tortoise and hare" step.  We start at the beginning of the array and try to find an intersection point in the cycle.
# Keep advancing 'slow' by one step and 'fast' by two steps until they meet inside the loop.
# Start up another pointer from the beginning of the array and march it forward until it hits the pointer inside the array.
# If the two hit, the intersection index is the duplicate element.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=fast=nums[0]
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow2,finder=slow,nums[0]
        while slow2!=finder:
            slow2=nums[slow2]
            finder=nums[finder]
        return finder
     
