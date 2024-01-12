'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.
Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.
Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
 
Constraints:
2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters.
'''

'''
Brief approach:
- Define a list of vowels.
- Calculate the midpoint of the string (n), which is half its length.
- Initialize counters (a_count and b_count) for vowels in the first and second halves, respectively.
- Iterate through the first half of the string and count the vowels in a_count.
- Iterate through the second half of the string and count the vowels in b_count.
- Check if the counts of vowels in both halves are equal.
- Return True if the counts are equal, indicating that the two halves have the same number of vowels; otherwise, return False.
'''

class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vowels=['a','e','i','o','u','A','E','I','O','U']
        n=len(s)//2
        a_count=0
        b_count=0
        for ch in s[:n]:
            if ch in vowels:
                a_count+=1
        for ch in s[n:]:
            if ch in vowels:
                b_count+=1
        if a_count==b_count:
            return True
        else:
            return False
