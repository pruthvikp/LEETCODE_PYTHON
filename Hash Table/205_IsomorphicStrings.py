'''
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
 
Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

# Approach:
# The approach used in this code is to iterate through each character of the strings s and t simultaneously. 
# For each character in s, it checks if the character is already in the dictionary d. 
# If it is not, it adds the character as a key to the dictionary d with its corresponding value being the character from t at the same index. 
# However, if the character is already in the dictionary d, it checks whether the value corresponding to that character is the same as the character from t at the same index. 
# If not, it returns False, indicating that the strings s and t are not isomorphic.
# If the loop completes without any mismatches, it returns True, indicating that the strings s and t are isomorphic.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i,ch in enumerate(s):
            if ch not in d and t[i] not in d.values():
                d[ch]=t[i]
            elif ch not in d and t[i] in d.values():
                return False
            elif d[ch]!=t[i]:
                return False
        return True
