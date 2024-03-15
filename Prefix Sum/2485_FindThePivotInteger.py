'''
Given a positive integer n, find the pivot integer x such that:
The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

Example 1:
Input: n = 8
Output: 6
Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.

Example 2:
Input: n = 1
Output: 1
Explanation: 1 is the pivot integer since: 1 = 1.

Example 3:
Input: n = 4
Output: -1
Explanation: It can be proved that no such integer exist.

Constraints:
1 <= n <= 1000
'''

# Approach:
# Calculate the total sum of integers from 1 to n using the formula (n * (n + 1)) / 2.
# Iterate through the integers from 1 to n and calculate the partial sum at each step using the same formula.
# If at any step the total sum plus the current integer is equal to twice the partial sum, return that integer as the pivot.
class Solution:
    def pivotInteger(self, n: int) -> int:
        total=(n*(n+1))/2
        for i in range(1,n+1):
            psum=(i*(i+1))/2
            if total+i==2*psum:
                return i
        return -1


# Approach:
# Calculate the total sum of integers from 1 to n using the formula (n+1)*n/2.
# Find the square root of the sum and convert it to an integer. This integer represents the pivot.
class Solution:
    def pivotInteger(self, n: int) -> int:
        sum = (n+1)*n/2
        pivot = int(math.sqrt(sum))
        return pivot if pivot*pivot == sum else -1
