'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

Example 2:
Input: arr = [1,2]
Output: false

Example 3:
Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 
Constraints:
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
'''

# The basic approach is to iterate through the sorted array and count the occurrences of each value. 
# The counts are then stored in a separate list (mylist), and if any count is repeated, the function returns False. 
# Otherwise, it returns True.

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        mylist=[]
        arr.sort()
        i=0
        n=len(arr)
        while i<n:
            rv=arr[i]
            rl=1
            while i+rl<n and arr[i+rl]==rv:
                rl+=1
            if rl in mylist:
                return False
            else:
                mylist.append(rl)
            i+=rl
        return True
