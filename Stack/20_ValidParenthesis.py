'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

# Approach:
# Initialize an empty stack to store opening parentheses, square brackets, and curly braces encountered while iterating through the string s.
# Iterate through each character c in the input string s.
# If c is an opening parenthesis, square bracket, or curly brace ('(', '[', '{'), push it onto the stack.
# If c is a closing parenthesis, square bracket, or curly brace (')', ']', '}'), perform the following checks:
# If the stack is empty, or the top element of the stack doesn't match the corresponding opening bracket for c, return False, indicating that the string is invalid.
# If the above checks pass, pop the top element from the stack.
# After iterating through all characters in the string, if the stack is empty, return True, indicating that the string is valid. Otherwise, return False.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or (c==')'and stack[-1]!='(') or (c==']' and stack[-1]!='[') or (c=='}' and stack[-1]!='{'):
                    return False
                stack.pop()
        return not stack
