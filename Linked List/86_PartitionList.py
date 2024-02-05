'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]
 
Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
'''

# Approach:
# The code iterates through the original list and creates two separate lists, one containing nodes with values less than x and the other containing nodes with values greater than or equal to x. 
# It then concatenates the two lists, maintaining the original order of elements, and returns the head of the modified list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        ptr=head
        head1=head2=None
        temp1=head1
        temp2=head2
        while ptr:
            new=ListNode(ptr.val)
            if ptr.val<x:
                if head1 is None:
                    head1=new
                    temp1=head1
                else:
                    temp1.next=new
                    temp1=temp1.next
            else:
                if head2 is None:
                    head2=new
                    temp2=head2
                else:
                    temp2.next=new
                    temp2=temp2.next
            ptr=ptr.next
        if temp1: 
            temp1.next=head2
            head=head1
        return head
