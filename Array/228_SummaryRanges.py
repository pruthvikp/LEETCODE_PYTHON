'''
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
 
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 
Constraints:
0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
'''

# This solution iterates through the sorted unique integer array. 
# It maintains a start value and a count value that tracks the expected value in the sequence. 
# It then iterates until the sequence breaks, indicating the end of a range. 
# For each range, it constructs the appropriate string representation based on whether the start and end values are equal. 
# Finally, it returns the list of constructed ranges.

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res=[]
        i=0
        while i<len(nums):
            start=nums[i]
            count=nums[i]
            while i<len(nums) and count==nums[i]:
                count+=1
                i+=1
            i-=1
            end=nums[i]
            if end==start:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{end}")
            i+=1
        return res
