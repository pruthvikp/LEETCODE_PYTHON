'''
You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
You should return the array of nums such that the the array follows the given conditions:
Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  

Example 2:
Input: nums = [-1,1]
Output: [1,-1]
Explanation:
1 is the only positive integer and -1 the only negative integer in nums.
So nums is rearranged to [1,-1].
 
Constraints:
2 <= nums.length <= 2 * 105
nums.length is even
1 <= |nums[i]| <= 105
nums consists of equal number of positive and negative integers.
 
It is not required to do the modifications in-place.
'''

# Brief approach:
# Initialize two lists to hold positive and negative numbers.
# Iterate through the input list and segregate positive and negative numbers into separate lists.
# Combine the positive and negative numbers alternately into the result list.
# Return the result list.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i=0
        pos,neg=[],[]
        while i<len(nums):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
            i+=1
        i=0
        res=[]
        while i<len(neg):
            res.extend([pos[i],neg[i]])
            i+=1
        return res

# Two pointer approach:
# It initializes a result list of zeros with the same length as the input array. 
# Then, it iterates through the input array, assigning positive numbers to even indices (starting from 0) and negative numbers to odd indices (starting from 1). 
# Finally, it returns the rearranged array.

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)
        i,j=0,1
        for num in nums:
            if num>0:
                res[i]=num
                i+=2
            else:
                res[j]=num
                j+=2
        return res
