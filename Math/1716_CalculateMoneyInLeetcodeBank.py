'''
Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
 
Constraints:
1 <= n <= 1000
'''

# Approach: 
# Maintain two variables, x for the number of weeks passed and y for the day within the week. 
# On each day, add the current amount to the total money, increment y, and if y becomes 7 (indicating Monday), increment x and reset y to 0.

class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        money=0
        x,y=0,0
        for i in range(n):
            money+=(x+y+1)
            y+=1
            if y%7==0:
                x+=1
                y=0
        return money
