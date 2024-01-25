'''
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:
Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:
Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
 
Constraints:
-231 <= n <= 231 - 1
 
Follow up: Could you solve it without loops/recursion?
'''

# Recursive Approach:
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        return n==1 or self.isPowerOfThree(n/3)

# Bit manipulation method: When we add previous power of three (in bit represenation) to left shift of previous power of three we get new power of three.
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        temp=1
        while n>1 and temp<n:
            temp+=temp<<1
        return temp==n
