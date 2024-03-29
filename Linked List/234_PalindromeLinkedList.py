'''
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 
Follow up: Could you do it in O(n) time and O(1) space?
'''

# The approach is to reverse the back half of the linked list to have the next attribute point to the previous node instead of the next node. 
# The first challenge then becomes finding the middle of the linked list in order to start our reversing process there. For that, we can look to Floyd's Cycle Detection Algorithm.

# With Floyd's, we'll travel through the linked list with two pointers, one of which is moving twice as fast as the other. When the fast pointer reaches the end of the list, the slow pointer must then be in the middle.
# Diagram 1 Withslow now at the middle, we can reverse the back half of the list with the help of another variable to contain a reference to the previous node (prev) and a three-way swap. Before we do this, however, we'll want to set prev.next = null, so that we break the reverse cycle and avoid an endless loop.
# Diagram 2 Once the back half is properly reversed andslow is once again at the end of the list, we can now start fast back over again at the head and compare the two halves simultaneously, with no extra space required.
# Diagram 3 If the two pointers ever disagree in value, we canreturn false, otherwise we can return true if both pointers reach the middle successfully.

# (Note: This process works regardless of whether the length of the linked list is odd or even, as the comparison will stop when slow reaches the "dead-end" node.)


# Code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        ptr=slow.next
        slow.next=None
        
        temp,temp2,temp3=None,ptr,ptr
        while temp2!=None:
            temp3=temp3.next
            temp2.next=temp
            temp=temp2
            temp2=temp3
        head2=temp

        while head and head2:
            if head.val!=head2.val:
                return False
            head,head2=head.next,head2.next
        return True

