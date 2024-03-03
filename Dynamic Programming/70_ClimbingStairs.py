'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Constraints:
1 <= n <= 45
'''

# Breakdown of code:
# The method climbStairs takes an integer n as input and returns an integer, which represents the number of distinct ways to climb to the top.
# If n is 0 or 1, there's only one way to climb the stairs (either not climbing any step or climbing just one step), so the function returns 1 in these cases.
# For n greater than 1, the variables prev and curr are initialized to represent the number of ways to climb the stairs with 1 and 2 steps respectively. Since there's only one way to climb 1 step and one way to climb 2 steps, both prev and curr are initially set to 1.
# A loop runs from 2 to n, inclusive. In each iteration, the variable temp stores the value of curr, curr is updated to the sum of prev and curr (representing the number of ways to climb the current step), and prev is updated to temp (representing the number of ways to climb the previous step).
# After the loop completes, curr holds the number of distinct ways to climb the staircase with n steps, so it's returned as the result.

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n+1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
