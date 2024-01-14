'''
Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)

You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

Example 1:
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"

Example 2:
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.

Example 3:
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
 
Constraints:
1 <= word1.length, word2.length <= 105
word1 and word2 contain only lowercase English letters.
'''

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if len(word1)!=len(word2):
            return False
        dic1={}
        for ch in word1:
            if ch in dic1:
                dic1[ch]+=1
            else:
                dic1[ch]=1
        dic2={}
        for ch in word2:
            if ch in dic2:
                dic2[ch]+=1
            else:
                dic2[ch]=1
        k1,k2=[],[]
        v1,v2=[],[]
        if len(dic1)==len(dic2):
            for key1 in dic1:
                k1.append(key1)
                v1.append(dic1[key1])
            for key2 in dic2:
                k2.append(key2)
                v2.append(dic2[key2])
            if sorted(v1)==sorted(v2) and sorted(k1)==sorted(k2):
                return True
        return False
