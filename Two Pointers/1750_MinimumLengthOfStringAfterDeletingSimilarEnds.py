'''
Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).

Example 1:
Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.

Example 2:
Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".

Example 3:
Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".
 
Constraints:
1 <= s.length <= 105
s only consists of characters 'a', 'b', and 'c'.
'''

# Brief approach:
# Initialize two pointers i and j at the start and end of the string, respectively.
# While i is less than j and the characters at i and j are the same, move i and j towards each other, skipping identical characters from both ends.
# Return the maximum of 0 and the length of the remaining substring between i and j (inclusive). 
# If the whole string is a palindrome, return 0. Otherwise, return the length of the remaining substring.

class Solution:
    def minimumLength(self, s: str) -> int:
        i,j=0,len(s)-1
        while i<j and s[i]==s[j]:
            while i<j and s[i]==s[i+1]:
                i+=1
            while i<j and s[j]==s[j-1]:
                j-=1
            i+=1
            j-=1
        else:
            return max(0,j-i+1)
