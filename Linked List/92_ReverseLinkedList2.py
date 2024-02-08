'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:
Input: head = [5], left = 1, right = 1
Output: [5]

Constraints:
The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

Follow up: Could you do it in one pass?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return 
        if head.next is None:
            return head
        m,n=left-1,right-1
        ptr=head
        if m!=0:
            for _ in range(m-1):
                ptr=ptr.next
            temp=ptr.next
        else:
            temp=ptr
        temp2=temp3=temp.next
        for _ in range(n-m):
            temp3=temp3.next
            temp2.next=temp
            temp=temp2
            temp2=temp3
        if m==0:
            head=temp
            ptr.next=temp3
        else:
            ptr.next.next=temp3
            ptr.next=temp
        return head
