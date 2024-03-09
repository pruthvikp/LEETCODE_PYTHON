'''
Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.

Example 2:
Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
 
Constraints:
1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.
'''

# The method first checks which input list is shorter and assigns it to variable l and the other list to variable s. 
# Then, it iterates over the elements of the shorter list and checks if each element is present in the set created from the longer list. 
# If a common element is found, it returns that element. 
# If no common element is found after iterating through all elements of the shorter list, it returns -1.
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1)<len(nums2):
            l=nums1
            s=set(nums2)
        else:
            l=nums2
            s=set(nums1)
        for num in l:
            if num in s:
                return num
        return -1

 # It creates a list containing the common elements of both input lists using set intersection (&), then returns the minimum element from that list if it's not empty, otherwise returns -1.
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums = list(set(nums1) & set(nums2))
        return min(nums) if nums else -1
