'''
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.

Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 
Constraints:
1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
'''

# Approach: 
# Reverse the input string s.
# Traverse the reversed string to find the length of the last word. 
# Start iterating from the beginning until a space character is encountered. 
# Then, continue iterating until the next space character is encountered or the end of the string is reached, counting the characters along the way.
# Return the length of the last word found.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s[::-1]
        length=0
        i=0
        while i<len(s):
            if s[i]==" ":
                i+=1
            else:
                while s[i]!=" ":
                    length+=1
                    i+=1
                return length
