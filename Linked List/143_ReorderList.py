'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
'''

# Approach:
# Find the middle by moving fast & slow iterators.
# Remember right part beginning and cut off left part from the right.
# Reverse right list, remember it new beginning.
# Iterate left part from beginning and right part merging right list nodes into left list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow,fast=head,head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        ptr=slow.next
        slow.next=None
        while fast.next:
            fast=fast.next

        temp=None
        temp2=temp3=ptr
        while temp2!=None:
            temp3=temp3.next
            temp2.next=temp
            temp=temp2
            temp2=temp3
        head2=temp

        dummy=temp=ListNode()
        tag=True
        while head and head2:
            if tag==True:
                temp.next=head
                temp=head
                head=head.next  
                tag=False              
            else:
                temp.next=head2
                temp=head2
                head2=head2.next
                tag=True
        temp.next=head if head else head2
        # return dummy.next
