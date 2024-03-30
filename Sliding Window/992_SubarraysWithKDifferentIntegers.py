'''
Given an integer array nums and an integer k, return the number of good subarrays of nums.
A good array is an array where the number of different integers in that array is exactly k.
For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:
Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 
Constraints:
1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
'''

# This algorithm counts subarrays with exactly k distinct elements by maintaining a sliding window with distinct elements.
# It calculates two results: one for the case where the number of distinct elements is strictly equal to k, 
# and another for the case where the number of distinct elements is greater than or equal to k.
# Finally, it returns the difference between the two results, which gives the count of subarrays with exactly k distinct elements.

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        left=right=res=0
        d={}
        while right<len(nums):
            d[nums[right]]=d.get(nums[right],0)+1
            while len(d)>k:
                d[nums[left]]-=1
                if d[nums[left]]==0:
                    del d[nums[left]]
                left+=1
            res+=(right-left+1)
            right+=1

        left=right=res2=0
        d={}
        while right<len(nums):
            d[nums[right]]=d.get(nums[right],0)+1
            while len(d)>=k:
                d[nums[left]]-=1
                if d[nums[left]]==0:
                    del d[nums[left]]
                left+=1
            res2+=(right-left+1)
            right+=1

        return res-res2
