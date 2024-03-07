'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
 
Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 
Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
'''

# Trivial method:
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares=[num**2 for num in nums]
        return sorted(squares)


# Two Pointer approach:
# Initialize two pointers, i and j, to traverse the input list nums. i starts from the first non-negative number, and j starts from the same position.
# If there are negative numbers in nums, decrement i to position it at the last negative number (or at 0 if all numbers are negative).
# Compare the squares of numbers at positions i and j. Append the smaller one to res and move the corresponding pointer.
# Repeat the above step until one of the pointers reaches either end of the list.
# If there are remaining elements after the loop, append them to res.
# Return res, which contains the sorted squares of the input list.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        while i<len(nums) and nums[i]<0:
            i+=1
        j=i
        if i!=0:
            i-=1
        res=[]
        if i!=j:
            while i>=0 and j<len(nums):
                if nums[j]**2<nums[i]**2:
                    res.append(nums[j]**2)
                    j+=1
                else:
                    res.append(nums[i]**2)
                    i-=1
            while i>=0:
                res.append(nums[i]**2)
                i-=1
        while j<len(nums):
            res.append(nums[j]**2)
            j+=1
        return res
