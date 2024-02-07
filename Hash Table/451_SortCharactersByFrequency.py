'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

Constraints:
1 <= s.length <= 5 * 105
s consists of uppercase and lowercase English letters and digits.
'''

# Approach:
# The Counter class from the collections module is used to count the occurrences of each character in the input string s. It creates a dictionary where keys are characters and values are their frequencies.
# The sorted function is then used to sort the dictionary items based on their values (frequencies) in descending order. This results in a list of tuples sorted by frequency.
# A string variable string is initialized to store the sorted string.
# The sorted list of tuples is iterated over, and for each tuple, the character is repeated its frequency number of times and appended to the string.
# Finally, the sorted string is returned.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d=Counter(s)
        d=sorted(d.items(), key=lambda x:x[1],reverse=True)
        string=""
        for i in range(len(d)):
            for _ in range(d[i][1]):
                string+=d[i][0]
        return string
