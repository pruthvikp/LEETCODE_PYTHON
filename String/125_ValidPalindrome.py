'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
'''

# This solution checks if a given string is a palindrome after converting it to lowercase and removing al non-alphanumeric characters. 

class Solution:
    def isPalindrome(self, s):
        s=s.lower()
        string=""
        for ch in s:
            if ch.isalnum():
                string+=ch
        i,j=0,-1
        while i<len(string)//2:
            if string[i]==string[j]:
                i+=1
                j-=1
            else:
                return False
        return True
