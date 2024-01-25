'''
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 105
'''

# Approach:
# Initialize variables mode, modefrequency, and iterate through the array.
# For each unique element, count its consecutive occurrences, runlength(rl) until a new element is encountered.
# If the runlength exceeds 25% of the array length, return the current element as the result. 
# Update mode and modefrequency accordingly. Return the final result.

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=len(arr)
        modefrequency=0
        i=0
        while i<n:
            rv=arr[i]
            rl=1
            while i+1<n and arr[i+1]==rv:
                i+=1
                rl+=1
                if rl>int(0.25*n):
                    return rv
            if rl>modefrequency:
                mode=rv
                modefrequency=rl
            i+=1
        return mode
