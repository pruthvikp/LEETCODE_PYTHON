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

# Brief Approach:
# Initialize an empty list res to store the result, calculate the sum of the array, and use a dictionary dic to track occurrences.
# Iterate through the array, if a number is already in the dictionary, append it to res as a duplicate; otherwise, add it to the dictionary and update the sum.
# Calculate the total sum using the arithmetic formula total = n * (n + 1) / 2 and append the missing number (total - sum) to res. Return the result.

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
        
