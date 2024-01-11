'''
Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


# Approach: 
# Convert the integer x to a string and use string slicing ([::-1]) to reverse the string. 
# Check if the original string is equal to its reverse and return True if it's a palindrome, False otherwise.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        if(x==x[::-1]):
            return True
        else:
            return False

        
