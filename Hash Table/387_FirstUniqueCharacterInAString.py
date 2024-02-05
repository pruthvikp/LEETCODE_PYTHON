'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1
 
Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
'''

# This solution utilizes a hashtable to store characters along with their occurrences and indices. 
# It iterates through the string to populate the hashtable. 
# Then, it iterates through the hashtable to find the first character with a count of 1, returning its index. 
# If no such character is found, it returns -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable={}
        for i,ch in enumerate(s):
            if ch in hashtable:
                hashtable[ch][1]+=1
            else:
                hashtable[ch]=[i,1]
        for key in hashtable:
            if hashtable[key][1]==1:
                return hashtable[key][0]
        return -1
