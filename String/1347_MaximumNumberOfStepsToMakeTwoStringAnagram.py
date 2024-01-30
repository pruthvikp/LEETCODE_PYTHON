'''
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.
Return the minimum number of steps to make t an anagram of s.
An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Example 1:
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
 
Constraints:
1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.
'''

# Approach:
# Initialize a variable count to keep track of the number of steps needed.
# Create two dictionaries dic1 and dic2 to count the occurrences of characters in strings s and t respectively.
# Iterate through string s and update the counts of characters in dic1.
# Similarly, iterate through string t and update the counts of characters in dic2.
# Iterate through the keys in dic1:
# -If the key is also present in dic2, compare the counts:
# -If the counts are equal, continue to the next key.
# -If the count in dic1 is greater than the count in dic2, add the difference to count.
# -If the key is not present in dic2, add the count from dic1 to count.
# Return the final value of count.

class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        count=0
        dic1={}
        for ch in s:
            if ch in dic1:
                dic1[ch]+=1
            else:
                dic1[ch]=1
        dic2={}
        for ch in t:
            if ch in dic2:
                dic2[ch]+=1
            else:
                dic2[ch]=1
        for key in dic1:
            if key in dic2:
                if dic1[key]==dic2[key]:
                    continue
                elif dic1[key]>dic2[key]:
                    count+=(dic1[key]-dic2[key])
            else:
                count+=dic1[key]
        return count
