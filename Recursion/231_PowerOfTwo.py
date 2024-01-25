'''
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false
 
Constraints:
-231 <= n <= 231 - 1
 '''

# Recursive Approach:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n==0 or n%2!=0:
            return False
        return self.isPowerOfTwo(n//2)

# Bit manipulation method:
# Bitwise AND operation: n & n-1 == 0
# When you subtract 1 from a power of two, you essentially flip the least significant bit (the rightmost bit that is set to 1) and set all the bits to its right to 1.
# For example, if n is 8 (binary: 1000), n-1 will be 7 (binary: 0111).
# When you perform a bitwise AND operation between n and n-1, you get zero only if n has only one bit set to 1.
# For any other number that is not a power of two, the result of the bitwise AND operation will not be zero because there will be other bits set to 1 in both n and n-1, causing the AND operation to yield a non-zero result.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        return n & n-1 == 0
