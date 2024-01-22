'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]

Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104
'''

# Approach:
# The solution involves iterating through the input array and keeping track of the occurrences of each number in a dictionary. 
# If a number is encountered more than once, it is added to the result list. 
# At the same time, the sum of all numbers in the array is calculated. 
# The missing number can be found by subtracting the sum from the expected sum of numbers from 1 to n.

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        n=len(nums)
        sum=0
        dic={}
        for num in nums:
            if num in dic:
                res.append(num)
            else:
                dic[num]=1
                sum+=num
        total=(n*(n+1))/2
        res.append(total-sum)
        return res
        
