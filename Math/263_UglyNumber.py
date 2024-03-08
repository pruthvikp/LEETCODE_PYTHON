'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
 
Constraints:
-231 <= n <= 231 - 1
'''

# Approach:
# If the input number n is 0, it's not considered an ugly number, so return False.
# Iterate through the list of prime factors [2, 3, 5].
# While n is divisible by any of these factors, divide n by that factor.
# After the loop, if n is 1, it means all prime factors are 2, 3, or 5, so return True; otherwise, return False.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return False
        for i in [2,3,5]:
            while n%i==0:
                n//=i
        return n==1
            
