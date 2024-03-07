'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 
Constraints:
1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

# Approach:
# Obtain the lengths of the haystack and needle strings, n and m.
# Loop through the haystack string up to the point where the needle could potentially be found.
# Within the loop, compare substrings of haystack with the needle. If a match is found, return the starting index i.
# If no match is found within the loop, return -1
  
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(haystack)
        m=len(needle)
        for i in range(n-m+1):
            j=0
            while j<m and needle[j]==haystack[i+j]:
                j+=1
            if j==m:
                return i
        return -1
