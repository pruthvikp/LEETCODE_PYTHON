'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 
Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

# Initialization: Initialize variables left, right, and res to 0. Create an empty dictionary d to store characters encountered in the substring.
# Sliding Window Technique: The solution uses the sliding window technique. The window is defined by the indices left and right, which represent the left and right boundaries of the substring being considered.
# Iterating through the String: Iterate over the string s using the right pointer until it reaches the end of the string.
# Checking for Repeated Characters: For each character s[right], check if it is not already present in the dictionary d. If it's not present, add it to d with a count of 1, indicating it's the first occurrence of that character in the current substring.
# Handling Repeated Characters: If s[right] is already present in d, it means we've encountered a repeating character. In this case, we need to shrink the window from the left until there are no repeating characters. This is done by incrementing left until s[left] becomes equal to s[right]. While incrementing left, we also remove the characters encountered from the dictionary d.
# Updating Maximum Length: After handling repeated characters (if any), update the maximum length res by taking the maximum of the current res and the length of the current substring (right - left + 1).
# Moving the Right Pointer: Increment the right pointer to consider the next character in the string.
# Returning the Result: Once the iteration over the string is complete, return the maximum length res, which represents the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,right=0,0
        res=0
        d={}
        while right<len(s):
            if s[right] not in d:
                d[s[right]]=1
            else:
                while s[left]!=s[right]:
                    del d[s[left]]
                    left+=1
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res

# Using set
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left,right=0,0
        res=0
        d=set()
        while right<len(s):
            if s[right] not in d:
                d.add(s[right])
            else:
                while s[left]!=s[right]:
                    d.remove(s[left])
                    left+=1
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res
