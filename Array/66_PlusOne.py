'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 
Constraints:
1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.
'''


'''
Approach 1:
- Initialize a variable sum with the value of the first digit in the input list (digits[0]).
- Iterate through the remaining digits in the input list using a for loop. Update sum by multiplying it by 10 and adding the current digit.
- Add 1 to the calculated sum.
- Empty the list digits.
- Use a while loop to extract digits from the sum and append them to the digits list until the sum becomes 0.
- Reverse the digits list.
- Return the resulting digits list.
'''

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        sum=digits[0]
        for i in range(1,len(digits)):
            sum=sum*10+digits[i]
        sum+=1
        digits=[]
        while sum!=0:
            digits.append(sum%10)
            sum=sum//10
        digits=digits[::-1]
        return (digits)

'''
Approach 2:
This approach directly modifies the input list, avoiding the need to convert the digits to an integer and then back to a list. 
It simulates the process of adding one to the number by incrementing the digits and handling any carryovers.
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        index=len(digits)-1
        while index>=0:
            num=digits[index]+1
            if num>9:
                digits[index]=0
                index-=1
            else:
                digits[index]=num
                break
        if index==-1:
            digits.insert(0,1)

        return digits
