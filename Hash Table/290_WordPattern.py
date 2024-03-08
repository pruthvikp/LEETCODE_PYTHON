'''
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
 
Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
'''

# Brief approach:
# Initialize an empty dictionary d.
# Split the string s into a list of words.
# Check if the lengths of the pattern and the list of words are equal; if not, return False.
# Iterate through the pattern and corresponding words in the list.
# For each character in the pattern, if it's not already in the dictionary and its corresponding word is not already used, add it to the dictionary. If it's already in the dictionary, check if its corresponding word matches; if not, return False.
# If all checks pass, return True.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d={}
        list1=s.split()
        if len(pattern)!=len(list1):
            return False
        i,n=0,len(pattern)
        while i<n:
            if pattern[i] not in d.keys() and list1[i] not in d.values():
                d[pattern[i]]=list1[i]
                i+=1
            elif pattern[i] in d and d[pattern[i]]==list1[i]:
                i+=1
                continue
            else:
                return False
        return True
