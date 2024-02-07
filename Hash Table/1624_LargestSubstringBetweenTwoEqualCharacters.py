'''
Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

Constraints:
1 <= s.length <= 300
s contains only lowercase English letters.
'''

# The approach is to iterate through the input string s and create a dictionary d where keys are characters from the string and values are lists of indices where those characters occur in the string.
# Then, it iterates through the dictionary and for each character that occurs more than once, it calculates the distance between the first and last occurrence of that character. 
# It keeps track of the longest distance found so far and returns it at the end.

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={}
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]]=[i]
        longest=-1
        for key in d:
            if len(d[key])>1:
                val=d[key][-1]-d[key][0]-1
                if val>longest:
                    longest=val
        return longest
