'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0
 
Constraints:
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
'''

# This approach converts the binary representation into its decimal equivalent by iterating through the linked list twice, once to find its length and then to compute the decimal value. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res=0
        n=0
        ptr=head
        while ptr.next:
            n+=1
            ptr=ptr.next
        while head:
            if head.val==1:
                res+=pow(2,n)
            n-=1
            head=head.next
        return res

# This approach directly converts the binary representation of the linked list into its decimal equivalent using string manipulation and conversion functions. 
# It doesn't require manually calculating powers of 2 as in the previous approach.

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        p = head
        ans = ''
        while p != None:
            ans += str(p.val)
            p = p.next
        return int(ans,2)

# This approach directly computes the decimal value of the linked list in a single pass without any string manipulation or conversion. 
# It efficiently builds the decimal value by shifting and adding bits as it traverses the linked list.

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 

'''
Visualization of algorithm of the above code-

Take For Example:
1101 -> 13

Binary View
0000 * 2 # shift left
0000 + 1 # add bit

0001 * 2 # shift left
0010 + 1 # add bit

0011 * 2 # shift left
0110 + 0 # add bit

0110 * 2 # shift left
1100 + 1 # add bit

1101 # 13

Decimal View
0 * 2 # x2
0 + 1 # add bit

1 * 2 # x2
2 + 1 # add bit

3 * 2 # x2
6 + 0 # add bit

6 * 2 # x2
12 + 1 # add bit

13 # Answer

'''
