'''
A string is a valid parentheses string (denoted VPS) if it meets one of the following:
It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:
depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.
Given a VPS represented as string s, return the nesting depth of s.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3

Constraints:
1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.
'''

# The approach essentially simulates the process of matching parentheses. 
# The maximum depth of nested parentheses is achieved when all opening parentheses are properly matched with corresponding closing parentheses. 
# The stack helps in keeping track of the depth as each opening parenthesis encountered contributes to an increase in depth, and each closing parenthesis encountered reduces the depth.
# The maximum depth encountered during traversal is stored in res and returned at the end.

class Solution:
    def maxDepth(self, s: str) -> int:
        stack=[]
        count,res=0,0
        for ch in s:
            if ch=='(':
                stack.append(ch)
                count+=1
                res=max(res,count)
            elif ch==')' and stack:
                stack.pop()
                count-=1
        return res
