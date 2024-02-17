'''
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

Example 1:
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.

Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 
Constraints:
1 <= arr.length <= 10^5
1 <= arr[i] <= 10^9
0 <= k <= arr.length
'''

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        di=Counter(arr)
        di = dict(sorted(di.items(), key=lambda x:x[1]))
        keys_to_remove = [key for key, value in di.items() if value == 1]
        for key in keys_to_remove:
            if k==0:
                break
            del di[key]
            k-=1            
        keys_to_remove=[]
        for key in di:
            if di[key]<=k:
                k-=di[key]
                keys_to_remove.append(key)
            else:
                break
        for key in keys_to_remove:
            del di[key]   
        return len(di)

# # Chatgpt
# Use a Counter to count the occurrences of each integer in the array.
# Sort the counts in ascending order.
# Iterate through the sorted counts:
# - If the current count is less than or equal to k, decrement k by the current count and reduce the number of unique integers left.
# - If the current count is greater than k, break the loop because we cannot remove more elements without exceeding k.
# Return the remaining count of unique integers.
  
from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        remaining_count = len(counter)        
        sorted_counts = sorted(counter.values())        
        for count in sorted_counts:
            if k >= count:
                k -= count
                remaining_count -= 1
            else:
                break       
        return remaining_count
