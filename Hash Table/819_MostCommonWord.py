'''
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.
The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:
Input: paragraph = "a.", banned = []
Output: "a"

Constraints:
1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.
'''

# Approach: 
# The code iterates through each character in the paragraph, building words until it encounters a non-alphabetic character. 
# It then checks if the word is in the banned list or not. If it's not banned, it updates a dictionary di to count the occurrences of each word.
# Finally, it finds the key (word) with the maximum value (frequency) in the dictionary and returns it as the most common word.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        di={}
        i=0
        while i<len(paragraph):
            string=""
            while i<len(paragraph) and paragraph[i].isalpha():
                string+=paragraph[i].lower()
                i+=1
            if string=="" or string in banned:
                i+=1
                continue
            elif string in di:
                di[string]+=1
            else:
                di[string]=1
            i+=1
        keymax = max(zip(di.values(), di.keys()))[1]
        return keymax
