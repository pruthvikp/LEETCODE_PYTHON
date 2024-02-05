'''
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:
Input: head = [1,1,2]
Output: [1,2]

Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
 
Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
'''

 # The code iterates through the list, and for each node, it checks if the next node has the same value. If it does, it updates the current node's next pointer to skip over the duplicate node. 
 # The process continues until the end of the list is reached. 
 # Finally, it returns the head of the modified list with duplicates removed.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr=head
        while ptr:
            temp=ptr
            data=ptr.val
            while temp and temp.val==data:
                temp=temp.next
            ptr.next=temp
            ptr=ptr.next
            if temp is None:
                return head
            if temp.next is None:
                ptr.next=None
                return head
        return head
