'''
Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
 
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself
'''

# The approach is to convert the binary strings a and b into decimal numbers, perform addition on those decimal numbers, and then convert the sum back into a binary string.
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x=0
        sum1=0
        for i in range(len(a)-1,-1,-1):
            sum1+=int(a[i])*(2**x)
            x+=1
        sum2=0
        x=0
        for i in range(len(b)-1,-1,-1):
            sum2+=int(b[i])*(2**x)
            x+=1
        sum=sum1+sum2
        if sum==0:
            return "0"
        strr=""
        while(sum!=0):
            strr=strr+str(sum%2)
            sum=sum//2
        return strr[::-1]

# This solution iterates through both strings simultaneously from right to left, adding corresponding bits along with the carry. 

class Solution(object):
    def addBinary(self, a, b):
        result = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            current_sum = digit_a + digit_b + carry
            result = str(current_sum % 2) + result
            carry = current_sum // 2
            i -= 1
            j -= 1
        
        return result





