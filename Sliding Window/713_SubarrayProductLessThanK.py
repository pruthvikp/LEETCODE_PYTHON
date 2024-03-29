'''
Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k. 

Example 1:
Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:
Input: nums = [1,2,3], k = 0
Output: 0 

Constraints:
1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
'''

# The algorithm initializes two pointers, left and right, to define the current subarray.
# Additionally, it initializes variables prod (to calculate the product of the elements within the current subarray) and res (to store the count of valid subarrays). 
# The algorithm iterates through the array, updating the product at each step by multiplying it with the element pointed to by the right pointer. 
# If the product exceeds or equals the threshold k, the algorithm advances the left pointer until the product becomes less than k. 
# At each iteration, the count of valid subarrays is updated based on the length of the current subarray.
# Finally, the function returns the total count of valid subarrays found.

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        left,right=0,0
        prod,res=1,0
        while right<len(nums):
            prod*=nums[right]
            while prod>=k:
                prod/=nums[left]
                left+=1
            res+=(right-left+1)
            right+=1
        return res
