'''
You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.

Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".

Constraints:
1 <= s.length <= 104
s[i] is either '0' or '1'.
'''

# The given code iterates through the string s twice: once assuming the first character is '0' and once assuming it is '1'. 
# During each iteration, it counts the number of operations needed to make the string alternating, considering the current character as the starting point. 
# It then returns the minimum count obtained from the two iterations.

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        if s[0]=='0':
            i=1
            while i<len(s):
                if i%2==1:
                    if s[i]=='0':
                        count+=1
                elif s[i]=='1':
                    count+=1
                i+=1
        else:
            i=1
            while i<len(s):
                if i%2==1:
                    if s[i]=='1':
                        count+=1
                elif s[i]=='0':
                    count+=1
                i+=1
        nextcount=0
        if s[0]=='1':
            i=0
            while i<len(s):
                if i%2==1:
                    if s[i]=='0':
                        nextcount+=1
                elif s[i]=='1':
                    nextcount+=1
                i+=1
        else:
            i=0
            while i<len(s):
                if i%2==1:
                    if s[i]=='1':
                        nextcount+=1
                elif s[i]=='0':
                    nextcount+=1
                i+=1
        return min(count,nextcount)

