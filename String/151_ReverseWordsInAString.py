'''
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 
Constraints:
1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 
Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?
'''

# Approach:
# Initialize variables i and li. i is used to iterate through the string, and li will store the words extracted from the string.
# Loop through the string while i is less than the length of the string.
# Inside the outer loop, skip over spaces using a nested while loop.
# Inside the nested loop, build up a word by appending characters until a space is encountered.
# Append the word to the li list if it's not empty.
# Outside the loop, construct the result string res by iterating through the words in li in reverse order and concatenating them with spaces.
# Return the result string.

class Solution:
    def reverseWords(self, s: str) -> str:
        i=0
        li=[]
        while i<len(s):
            while i<len(s) and s[i]==" ":
                i+=1
            string=""
            while i<len(s) and s[i]!=" ":
                string+=s[i]
                i+=1
            if string!="":
                li.append(string)
            i+=1
        res=""
        for string in li[:0:-1]:
            res+=(string+" ")
        return res+(li[0])        

# Split the input string s into individual words using the split() method, considering space as the delimiter.
# Reverse the order of the obtained list of words.
# Filter out any empty strings from the reversed list.
# Join the non-empty words back together with a space separator to form the reversed string.
# Return the reversed string.
class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split(' ')
        word_list = []
        for word in split_s[::-1]:
            if word != '':
                word_list.append(word)
        reverse_str = ' '.join(word_list)
        return reverse_str

# One line soln
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
