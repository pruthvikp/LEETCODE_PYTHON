'''
You are given an integer array nums and a positive integer k.
Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.
A subarray is a contiguous sequence of elements within an array.

Example 1:
Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].

Example 2:
Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.
 
Constraints:
1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
'''

# Approach:
# Solve the reverse question by sliding window.
# Solve for number of subarrays where the maximum appears less than k times and return total number of possible subarrays minus the answer you got

# Iterate through the array using the right pointer.
# Increment count if the current element is equal to the maximum element.
# If count becomes greater than or equal to k, start incrementing the left pointer until count becomes less than k. 
# At each step, update the result by adding the length of the subarray.
# This gives the number of subarrays where the maximum appears less than k times, 
# Return the total number of subarrays minus the result obtained.

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left,right=0,0
        res,count=0,0
        maxi=max(nums)
        n=len(nums)
        while right<n:
            if nums[right]==maxi:
                count+=1
            while count>=k:
                if nums[left]==maxi:
                    count-=1
                left+=1      
            res+=(right-left+1)
            right+=1
        return (n*(n+1)//2)-res
