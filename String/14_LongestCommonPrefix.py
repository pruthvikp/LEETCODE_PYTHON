'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

#  Approach involves comparing characters in each string with the corresponding characters in the first string (x) until a mismatch is found. 
# The common prefix found so far is updated in x, and the process continues until all strings are processed. 
# The final value of x is the longest common prefix.

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        x=strs[0]
        strs=strs[1:]
        string=""
        for c in strs:
            for i in range(len(min(x,c))):
                if x[i]==c[i]:
                    string+=x[i]
                else:
                    break
            x=string
            string=""
        return x
