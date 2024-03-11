'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 
Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

# Brief Approach:
# Create a Counter dictionary d for string s.
# Initialize a variable sum to store the length of the longest palindrome.
# Initialize a flag variable flag to track if there's been an odd count character encountered yet.
# Iterate through the keys in the dictionary. If the count of a character is odd and flag is 0, add the count to sum and set flag to 1.
# If the count is even, add it directly to sum. If the count is odd and flag is already 1, add count - 1 to sum.
# Return sum, which represents the length of the longest palindrome possible.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=Counter(s)
        sum=0
        flag=0
        for key in d:
            if flag==0 and d[key]%2==1:
                sum+=d[key]
                flag=1
            elif d[key]%2==0:
                sum+=d[key]
            else:
                sum+=d[key]-1
        return sum
